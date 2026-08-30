from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from datetime import datetime, timezone
from time import monotonic
from typing import Any, Callable
from urllib.parse import urlparse
from urllib.request import urlopen


class SlidingWindowRateLimiter:
    def __init__(self, limit: int, window_seconds: float = 60) -> None:
        if limit < 1 or window_seconds <= 0:
            raise ValueError("limit and window must be positive")
        self.limit = limit
        self.window_seconds = window_seconds
        self._events: dict[str, deque[float]] = defaultdict(deque)

    def allow(self, key: str, now: float | None = None) -> bool:
        current = monotonic() if now is None else now
        events = self._events[key]
        while events and events[0] <= current - self.window_seconds:
            events.popleft()
        if len(events) >= self.limit:
            return False
        events.append(current)
        return True


class MetricsRegistry:
    def __init__(self) -> None:
        self.counters: dict[str, int] = defaultdict(int)
        self.observations: dict[str, list[float]] = defaultdict(list)

    def increment(self, name: str, amount: int = 1) -> None:
        self.counters[name] += amount

    def observe(self, name: str, value: float) -> None:
        self.observations[name].append(value)

    def snapshot(self) -> dict[str, object]:
        return {"counters": dict(self.counters), "observations": dict(self.observations)}


class StructuredLogger:
    def __init__(self, service: str) -> None:
        if not service:
            raise ValueError("service name is required")
        self.service = service
        self._events: list[dict[str, Any]] = []

    def emit(self, event: str, message: str, **fields: Any) -> dict[str, Any]:
        payload = {
            "service": self.service,
            "event": event,
            "message": message,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
        payload.update(fields)
        self._events.append(payload)
        return payload

    def snapshot(self) -> list[dict[str, Any]]:
        return list(self._events)


@dataclass(frozen=True)
class DependencyStatus:
    name: str
    ready: bool
    detail: str


def tcp_like_readiness(name: str, url: str, timeout: float = 1.0, opener: Callable = urlopen) -> DependencyStatus:
    try:
        with opener(url, timeout=timeout):
            return DependencyStatus(name, True, "reachable")
    except Exception as error:
        return DependencyStatus(name, False, str(error))


def redis_readiness(
    name: str,
    url: str,
    timeout: float = 1.0,
    ping: Callable[[str], bool] | None = None,
) -> DependencyStatus:
    if not name or not url:
        raise ValueError("name and redis url are required")
    try:
        parsed = urlparse(url)
        if ping is not None:
            ready = bool(ping(url))
        else:
            ready = bool(parsed.scheme in {"redis", "rediss"} and parsed.netloc)
        if ready:
            return DependencyStatus(name, True, f"redis reachable at {url} (timeout={timeout})")
        return DependencyStatus(name, False, f"redis unreachable at {url}")
    except Exception as error:
        return DependencyStatus(name, False, str(error))

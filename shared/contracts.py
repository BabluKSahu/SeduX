"""Dependency-free contracts for the SeduX control plane."""

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from typing import Any


@dataclass(frozen=True)
class ServiceStatus:
    name: str
    status: str
    version: str = "0.1.0"

    def to_dict(self) -> dict[str, str]:
        return asdict(self)


SERVICE_NAMES = (
    "gateway",
    "voice",
    "avatar",
    "llm",
    "emotion",
    "task",
    "home",
    "screen",
)


def health_payload(service: str) -> dict[str, Any]:
    return {
        "service": service,
        "status": "ok",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "version": "0.1.0",
    }
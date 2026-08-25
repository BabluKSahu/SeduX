# SeduX Implementation Backlog

This backlog translates the build guide into 15 implementation tracks. A track is complete only when its tests, security checks, and operational documentation pass.

## Part 1: Vision, Scope, and Acceptance Criteria
- [x] Record product scope and target outcomes.
- [x] Define the first executable milestone: a health-checked control plane.
- [ ] Replace aspirational metrics with reproducible benchmark definitions.
- [ ] Document supported platforms, non-goals, and consent boundaries.

## Part 2: System Architecture
- [x] Add shared service status and health contracts.
- [x] Add a gateway health endpoint.
- [ ] Add versioned REST and WebSocket schemas, request IDs, timeouts, retries, and tracing.
- [ ] Validate the architecture with a local end-to-end test.

## Part 3: Backend Infrastructure
- [ ] Create FastAPI entry points with typed settings and lifecycle hooks.
- [ ] Add PostgreSQL migrations for users, conversations, messages, tasks, memory, and audit logs.
- [ ] Add Redis connectivity, rate limiting, queues, structured logs, metrics, and readiness probes.
- [ ] Add CPU-only and GPU Docker Compose profiles.

## Part 4: Frontend and User Interface
- [ ] Scaffold an accessible React and TypeScript client.
- [ ] Build chat, service status, task, home, screen, and settings views.
- [ ] Add typed WebSocket reconnection and responsive visual regression tests.
- [ ] Keep model and device controls consent-driven.

## Part 5: 3D Avatar and Motion
- [ ] Add a placeholder avatar scene and documented GLB asset contract.
- [ ] Implement avatar state transitions and deterministic animation replay.
- [ ] Add blend-shape and viseme mapping.
- [ ] Add frame-time telemetry and low-performance fallback validation.

## Part 6: Emotion Detection and Expression
- [ ] Define modality result schemas and confidence semantics.
- [ ] Implement CPU-safe text emotion analysis first.
- [ ] Implement confidence-aware fusion with missing-input handling.
- [ ] Add optional face, voice, gaze, consent, retention, and accuracy fixtures.

## Part 7: Voice Pipeline
- [ ] Define streaming audio, transcript, TTS, and viseme events.
- [ ] Add CI-safe STT and TTS test doubles.
- [ ] Implement VAD, backpressure, cancellation, and bounded buffers.
- [ ] Add optional local and cloud adapters with latency measurements.

## Part 8: Screen Automation and Device Access
- [ ] Define capability-based actions and immutable audit events.
- [ ] Implement read-only screenshot and OCR interfaces.
- [ ] Require confirmation for submit, destructive, and system actions.
- [ ] Add dry-run, target verification, rate limits, emergency stop, and sandboxing.

## Part 9: Task Scheduling and Orchestration
- [ ] Add typed task lifecycle and execution contracts.
- [ ] Implement one-time and recurring schedules with timezone correctness.
- [ ] Add idempotency, retries, dead letters, conflict detection, and history.
- [ ] Test restarts, duplicate delivery, and daylight-saving changes.

## Part 10: Memory and Personality
- [ ] Implement bounded short-term context.
- [ ] Add explicit memory creation, retrieval, correction, export, and deletion.
- [ ] Add replaceable embedding and graph adapters.
- [ ] Test user isolation and sensitive-memory exclusion.

## Part 11: Home Automation
- [ ] Define normalized device, capability, state, and scene schemas.
- [ ] Add Home Assistant and MQTT adapters with permission checks.
- [ ] Add stale-state, unavailable-device, duplicate-command, and rollback tests.
- [ ] Confirm sensitive actions such as locks and alarms.

## Part 12: Security, Privacy, and Governance
- [ ] Add authentication, refresh rotation, roles, and scopes.
- [ ] Add secure secret and encryption-key handling.
- [ ] Add consent, retention, export, deletion, redaction, and audit workflows.
- [ ] Run dependency, container, API, and threat-model reviews.

## Part 13: Development Roadmap
- [x] Establish this dependency-aware 15-part backlog.
- [ ] Convert tracks into milestone issues with owners and exit criteria.
- [ ] Add CI gates for formatting, typing, tests, and security.
- [ ] Track latency, reliability, task success, and privacy metrics from day one.

## Part 14: Technology Stack
- [ ] Pin supported runtime, database, cache, and adapter versions.
- [ ] Separate CPU dependencies from optional GPU and cloud dependencies.
- [ ] Record licenses, model terms, data usage, and provenance.
- [ ] Add upgrade tests and a hardware compatibility matrix.

## Part 15: Implementation, Testing, and Operations
- [x] Add a dependency-free smoke-testable gateway foundation.
- [ ] Add Dockerfiles, environment templates, setup commands, and migrations.
- [ ] Add unit, integration, end-to-end, load, and failure-injection tests.
- [ ] Add backups, observability, health checks, rollback runbooks, and deployment validation.

## Current Build Slice

The first slice is independent of external services and model weights. It provides shared contracts, a gateway health endpoint, a service registry, and executable contract tests.# SeduX Implementation Backlog

This backlog translates the build guide into 15 implementation tracks. Work is ordered by dependency, and a track is complete only when its tests, security checks, and operational documentation pass.

## Part 1: Vision, Scope, and Acceptance Criteria

- [x] Record the product scope and target outcomes in the build guide.
- [x] Define the first executable milestone: health-checked service control plane.
- [ ] Replace aspirational metrics with benchmark definitions and reproducible test fixtures.
- [ ] Document supported platforms, explicit non-goals, and consent boundaries.

## Part 2: System Architecture

- [x] Add a shared service registry and health contract.
- [x] Add a gateway health endpoint for the control plane.
- [ ] Add versioned REST and WebSocket schemas.
- [ ] Add request IDs, timeouts, retries, and tracing across service boundaries.
- [ ] Validate the architecture with an end-to-end local compose test.

## Part 3: Backend Infrastructure

- [ ] Create FastAPI service entry points with typed settings and lifecycle hooks.
- [ ] Add PostgreSQL migrations for users, conversations, messages, tasks, memory, and audit logs.
- [ ] Add Redis connectivity, rate limiting, and durable queue conventions.
- [ ] Add Docker Compose profiles for CPU-only development and GPU workloads.
- [ ] Add structured logging, metrics, and readiness probes.

## Part 4: Frontend and User Interface

- [ ] Scaffold the React and TypeScript client with accessible navigation.
- [ ] Build chat, service status, task, home, screen, and settings views.
- [ ] Add WebSocket reconnection and typed event handling.
- [ ] Add responsive visual regression tests and keyboard navigation checks.
- [ ] Keep model and device controls visibly consent-driven.

## Part 5: 3D Avatar and Motion

- [ ] Add a placeholder avatar scene with a documented GLB asset contract.
- [ ] Implement idle, listening, thinking, speaking, reacting, and sleeping states.
- [ ] Add blend-shape and viseme mapping with a deterministic replay fixture.
- [ ] Add frame-time telemetry and low-performance fallback behavior.
- [ ] Validate rendering on supported desktop and mobile browsers.

## Part 6: Emotion Detection and Expression

- [ ] Define versioned modality result schemas and confidence semantics.
- [ ] Implement text emotion analysis as the first CPU-safe modality.
- [ ] Implement confidence-aware multimodal fusion with missing-input handling.
- [ ] Add face, voice, and gaze adapters behind optional dependencies.
- [ ] Add privacy consent, retention, and accuracy evaluation fixtures.

## Part 7: Voice Pipeline

- [ ] Define streaming audio, transcript, TTS, and viseme event schemas.
- [ ] Add a local test double for STT and TTS so CI needs no model weights.
- [ ] Implement VAD, streaming backpressure, cancellation, and bounded buffers.
- [ ] Add optional Whisper, CosyVoice, and cloud provider adapters.
- [ ] Measure end-to-end latency with audio fixtures and publish budgets.

## Part 8: Screen Automation and Device Access

- [ ] Define a capability-based action model and immutable audit events.
- [ ] Implement read-only screenshot and OCR interfaces behind explicit permissions.
- [ ] Require confirmation for submit, destructive, and system actions.
- [ ] Add dry-run mode, target verification, rate limits, and emergency stop.
- [ ] Run automation only in a sandbox with scoped filesystem and network access.

## Part 9: Task Scheduling and Orchestration

- [ ] Add typed task creation, update, cancellation, and execution contracts.
- [ ] Implement one-time and recurring schedules with timezone correctness.
- [ ] Add idempotency keys, retries, dead-letter handling, and conflict detection.
- [ ] Add user-visible notifications and execution history.
- [ ] Test daylight-saving changes, restarts, and duplicate delivery.

## Part 10: Memory and Personality

- [ ] Implement short-term conversation context with bounded retention.
- [ ] Add explicit memory creation, retrieval, correction, export, and deletion.
- [ ] Add embedding and graph adapters behind replaceable interfaces.
- [ ] Implement personality settings with safe, predictable adaptation rules.
- [ ] Add tests proving user isolation and sensitive-memory exclusion.

## Part 11: Home Automation

- [ ] Define normalized device, capability, state, and scene schemas.
- [ ] Add a Home Assistant adapter with connection and permission checks.
- [ ] Add MQTT topic validation and reconnect behavior.
- [ ] Implement confirmation for locks, alarms, purchases, and other sensitive actions.
- [ ] Test stale state, unavailable devices, duplicate commands, and rollback behavior.

## Part 12: Security, Privacy, and Governance

- [ ] Add authentication, refresh-token rotation, and role/scope authorization.
- [ ] Add secret validation, encryption-key handling, and secure defaults.
- [ ] Add consent records, retention jobs, export, and deletion workflows.
- [ ] Add audit logging with tamper-aware storage and redaction.
- [ ] Run dependency, container, API, and threat-model reviews before production.

## Part 13: Development Roadmap

- [x] Establish a dependency-aware backlog for all 15 parts.
- [ ] Convert the backlog into milestone-sized issues with owners and exit criteria.
- [ ] Add CI gates for formatting, typing, unit tests, integration tests, and security.
- [ ] Track latency, reliability, task success, and privacy metrics from the first vertical slice.

## Part 14: Technology Stack

- [ ] Pin supported Python, Node, database, cache, and model adapter versions.
- [ ] Separate required CPU dependencies from optional GPU and cloud dependencies.
- [ ] Record licenses, model terms, data usage, and provenance for every model.
- [ ] Add upgrade tests and a compatibility matrix for supported hardware.

## Part 15: Implementation, Testing, and Operations

- [x] Add a dependency-free smoke-testable gateway foundation.
- [ ] Add service Dockerfiles, local environment templates, and reproducible setup commands.
- [ ] Add unit, integration, end-to-end, load, and failure-injection tests.
- [ ] Add migrations, backups, health checks, observability, and rollback runbooks.
- [ ] Complete the deployment checklist only after production-like validation passes.

## Current Build Slice

The repository currently contains the shared contract module, a standard-library gateway, and contract tests. These deliberately avoid external services and model weights so the first validation can run in a clean Python environment.
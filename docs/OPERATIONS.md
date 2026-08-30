# Operations Runbook

## Setup and Validation

```bash
cp .env.example .env
python -m pip install '.[dev]'
python -m unittest discover -s tests -v
docker compose --profile cpu up --build
```

Use `docker compose --profile gpu up gpu-worker` only on a host with the NVIDIA container runtime. Validate `/health`, `/readiness`, and `/metrics` before routing traffic.

## Backup and Restore

Create encrypted PostgreSQL backups with `pg_dump --format=custom`; snapshot model/config volumes separately. Test restores into an isolated database before each release. Redis is treated as rebuildable cache/queue state; durable task definitions remain in PostgreSQL.

## Rollback

Retain the previous immutable image and migration backup. Stop ingress, roll application containers back first, and reverse a migration only when its matching down migration has been rehearsed. Otherwise restore the database backup, then rerun health and end-to-end checks.

## Incident Controls

Disable screen and home scopes first for suspected compromise. Rotate `SEDUX_AUTH_SECRET` and external credentials, revoke active sessions, preserve redacted audit logs, and restore service only after readiness and consent-path tests pass.
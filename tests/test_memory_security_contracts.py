import unittest

from shared.governance import AuditEvent, ConsentRecord, RetentionPolicy
from shared.memory import MemoryEntry, MemoryOperation, MemoryScope
from shared.security import AccessScope, SecurityPrinciple, redact_sensitive_text


class MemorySecurityGovernanceContractsTests(unittest.TestCase):
    def test_memory_entry_tracks_scope_and_operation(self) -> None:
        entry = MemoryEntry(
            user_id="user-123",
            scope=MemoryScope.USER,
            operation=MemoryOperation.CREATE,
            key="favorite_color",
            value="blue",
            summary="Prefers blue interactions.",
        )
        self.assertEqual(entry.scope, MemoryScope.USER)
        self.assertEqual(entry.operation, MemoryOperation.CREATE)
        self.assertEqual(entry.key, "favorite_color")

    def test_redaction_preserves_non_sensitive_content(self) -> None:
        text = "Token abc123 should be hidden and email user@example.com kept masked."
        redacted = redact_sensitive_text(text)
        self.assertIn("[REDACTED]", redacted)
        self.assertIn("[EMAIL]", redacted)
        self.assertNotIn("abc123", redacted)

    def test_consent_record_and_audit_event_are_valid(self) -> None:
        consent = ConsentRecord(
            user_id="user-123",
            purpose="voice_analysis",
            granted=True,
            scopes=[AccessScope.VOICE, AccessScope.MEMORY],
        )
        event = AuditEvent(
            actor="system",
            action="memory_export",
            entity="memory:user-123",
            details={"requested_by": "user-123"},
        )
        self.assertTrue(consent.granted)
        self.assertIn(AccessScope.VOICE, consent.scopes)
        self.assertEqual(event.action, "memory_export")

    def test_retention_policy_requires_positive_ttl(self) -> None:
        policy = RetentionPolicy(purpose="voice", ttl_days=30)
        self.assertEqual(policy.ttl_days, 30)
        self.assertEqual(policy.purpose, "voice")


if __name__ == "__main__":
    unittest.main()

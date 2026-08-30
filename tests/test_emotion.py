import json
import threading
import unittest
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from services.emotion.main import create_server
from shared.emotion import EmotionLabel, analyze_text_emotion


class EmotionTests(unittest.TestCase):
    def test_text_analyzer_returns_confident_bounded_result(self) -> None:
        result = analyze_text_emotion("I am excited and happy!")
        self.assertEqual(result.dominant, EmotionLabel.HAPPY)
        self.assertGreater(result.confidence, 0.5)
        self.assertTrue(0.0 <= result.intensity <= 1.0)
        self.assertTrue(-1.0 <= result.valence <= 1.0)

    def test_empty_text_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            analyze_text_emotion("  ")

    def test_emotion_service_analyzes_text_over_http(self) -> None:
        server = create_server(port=0)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            request = Request(
                f"http://127.0.0.1:{server.server_port}/emotion/analyze",
                data=json.dumps({"text": "I feel worried and nervous"}).encode(),
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            with urlopen(request) as response:
                payload = json.load(response)
            self.assertEqual(payload["dominant"], "anxious")
            self.assertIn("confidence", payload)
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=2)

    def test_emotion_service_rejects_invalid_text(self) -> None:
        server = create_server(port=0)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            request = Request(
                f"http://127.0.0.1:{server.server_port}/emotion/text",
                data=json.dumps({"text": ""}).encode(),
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            with self.assertRaises(HTTPError) as context:
                urlopen(request)
            self.assertEqual(context.exception.code, 400)
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=2)

    def test_emotion_service_rejects_non_object_json(self) -> None:
        server = create_server(port=0)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            request = Request(
                f"http://127.0.0.1:{server.server_port}/emotion/text",
                data=b"[]",
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            with self.assertRaises(HTTPError) as context:
                urlopen(request)
            self.assertEqual(context.exception.code, 400)
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=2)


if __name__ == "__main__":
    unittest.main()

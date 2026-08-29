from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_multimodal_missing_text():
    r = client.post("/engine/multimodal", json={"mode":"sovereign"})
    assert r.status_code == 422


def test_multimodal_text_type():
    r = client.post("/engine/multimodal", json={"text": 123, "mode":"sovereign"})
    assert r.status_code == 422


def test_multimodal_long_text():
    long_text = "x" * 10000
    r = client.post("/engine/multimodal", json={"text": long_text, "mode":"sovereign"})
    assert r.status_code == 200
    assert r.json().get("input") == long_text

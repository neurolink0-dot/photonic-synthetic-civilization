from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json().get("status") == "ok"


def test_status():
    r = client.get("/status")
    assert r.status_code == 200
    j = r.json()
    assert j.get("engine") == "HRQ Dynasty"


def test_multimodal():
    r = client.post("/engine/multimodal", json={"text": "hello", "mode": "sovereign"})
    assert r.status_code == 200
    j = r.json()
    assert j.get("input") == "hello"
    assert "HRQ Dynasty received" in j.get("response", "")


def test_karma():
    r = client.get("/karma/")
    assert r.status_code == 200
    assert r.json().get("karma") == 0

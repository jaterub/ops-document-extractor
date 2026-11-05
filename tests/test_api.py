from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_returns_ok():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_documents_returns_labelled_dataset():
    response = client.get("/documents")
    assert response.status_code == 200
    records = response.json()
    assert len(records) == 6
    assert {record["document_type"] for record in records} == {"invoice", "contract"}

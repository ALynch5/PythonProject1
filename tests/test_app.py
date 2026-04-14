# Colin editing this here to finally double check, 14/04
from app import app

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200


def test_status():
    client = app.test_client()
    response = client.get("/status")
    assert response.status_code == 200

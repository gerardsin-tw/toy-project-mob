from fastapi.testclient import TestClient
from app.main import app
import sys

client = TestClient(app)

def test_trivia():
    response = client.get("/trivia")
    assert response.status_code == 200

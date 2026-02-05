from fastapi.testclient import TestClient
from src.main import app
from src.models.user import User
from src.config.database import get_session
from sqlmodel import Session
from unittest.mock import patch


def test_read_main():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Todo API is running!"}


def test_health_check():
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
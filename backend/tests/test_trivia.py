from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch, AsyncMock
import httpx

client = TestClient(app)

@patch('httpx.AsyncClient.get')
def test_trivia_multiple_questions(mock_get):
    mock_response = AsyncMock()
    mock_response.json = lambda: {
        "results": [
        {"type": "multiple",
        "difficulty": "easy",
        "category": "General Knowledge",
        "question": "What is the name of the Jewish New Year?",
        "correct_answer": "Rosh Hashanah",
        "incorrect_answers": [
        "Elul",
        "New Year",
        "Succoss"
    ]},
        {"type": "multiple",
        "difficulty": "easy",
        "category": "General Knowledge",
        "question": "The file hosting service, &quot;Google Drive&quot; was launched on what day?",
        "correct_answer": "April 24, 2012",
        "incorrect_answers": [
        "January 12, 2014",
        "November 14, 2008",
        "January 20, 2010"
    ]}
    ]
    }
    mock_response.raise_for_status = AsyncMock()
    mock_get.return_value = mock_response
    
    response = client.get("/trivia")
    assert response.status_code == 200
    assert len(response.json()) == 2

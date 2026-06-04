from fastapi.testclient import TestClient
from app.service import TriviaService
from unittest.mock import patch, AsyncMock
import pytest

@pytest.mark.asyncio
async def test_fetch_trivia(httpx_mock):
    mock_response=  {
        "response_code": 0,
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
    ]}
    ]
    }
    httpx_mock.add_response(url="https://opentdb.com/api.php?amount=1&type=multiple", json=mock_response)
    
    service = TriviaService(base_url="https://opentdb.com/api.php")
    questions = await service.fetch_trivia(amount=1)
    
    assert len(questions) == 1
    assert questions[0]["question"] == "What is the name of the Jewish New Year?"
    assert questions[0]["correct_answer"] == "Rosh Hashanah"
    assert "Rosh Hashanah" in questions[0]["all_answers"]
    assert len(questions[0]["all_answers"]) == 4

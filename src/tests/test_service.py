from fastapi.testclient import TestClient
from app.service import TriviaService
from unittest.mock import patch, AsyncMock
import pytest


@pytest.mark.asyncio
async def test_fetch_trivia(httpx_mock):
    mock_response = {
        "response_code": 0,
        "results": [
            {
                "type": "multiple",
                "difficulty": "easy",
                "category": "General Knowledge",
                "question": "What is the name of the Jewish New Year?",
                "correct_answer": "Rosh Hashanah",
                "incorrect_answers": ["Elul", "New Year", "Succoss"],
            }
        ],
    }
    httpx_mock.add_response(
        url="https://opentdb.com/api.php?amount=1&type=multiple&category=9",
        json=mock_response,
    )

    service = TriviaService(base_url="https://opentdb.com/api.php")
    questions = await service.fetch_trivia(amount=1, type="multiple", category=9)

    assert questions[0]["question"] == "What is the name of the Jewish New Year?"
    assert questions[0]["correct_answer"] == "Rosh Hashanah"
    assert "Rosh Hashanah" in questions[0]["all_answers"]
    assert len(questions[0]["all_answers"]) == 4


@pytest.mark.asyncio
async def test_fetch_trivia_number_of_questions(httpx_mock):
    mock_response = {
        "response_code": 0,
        "results": [
            {
                "type": "boolean",
                "difficulty": "easy",
                "category": "General Knowledge",
                "question": "Nutella is produced by the German company Ferrero.",
                "correct_answer": "False",
                "incorrect_answers": ["True"],
            },
            {
                "type": "boolean",
                "difficulty": "easy",
                "category": "General Knowledge",
                "question": "March 10th is also known as Mar10 Day.",
                "correct_answer": "True",
                "incorrect_answers": ["False"],
            },
        ],
    }
    httpx_mock.add_response(
        url="https://opentdb.com/api.php?amount=2&type=multiple&category=9",
        json=mock_response,
    )

    service = TriviaService(base_url="https://opentdb.com/api.php")
    questions = await service.fetch_trivia(amount=2, type="multiple", category=9)

    assert len(questions) == 2


@pytest.mark.asyncio
async def test_fetch_trivia_type_boolean(httpx_mock):
    mock_response = {
        "response_code": 0,
        "results": [
            {
                "type": "boolean",
                "difficulty": "easy",
                "category": "General Knowledge",
                "question": "&quot;27 Club&quot; is a term used to refer to a list of famous actors, musicians, and artists who died at the age of 27.",
                "correct_answer": "True",
                "incorrect_answers": ["False"],
            }
        ],
    }
    httpx_mock.add_response(
        url="https://opentdb.com/api.php?amount=1&type=boolean&category=9",
        json=mock_response,
    )

    service = TriviaService(base_url="https://opentdb.com/api.php")
    questions = await service.fetch_trivia(amount=1, type="boolean", category=9)

    assert questions[0]["type"] == "boolean"
    assert questions[0]["correct_answer"] == "True"
    assert sorted(questions[0]["all_answers"]) == ["False", "True"]


@pytest.mark.asyncio
async def test_fetch_trivia_category(httpx_mock):
    mock_response = {
        "response_code": 0,
        "results": [
            {
                "type": "boolean",
                "difficulty": "easy",
                "category": "Entertainment: Film",
                "question": "Actor Tommy Chong served prison time.",
                "correct_answer": "True",
                "incorrect_answers": ["False"],
            }
        ],
    }
    httpx_mock.add_response(
        url="https://opentdb.com/api.php?amount=1&type=multiple&category=11",
        json=mock_response,
    )

    service = TriviaService(base_url="https://opentdb.com/api.php")
    questions = await service.fetch_trivia(amount=1, type="multiple", category=11)

    assert questions[0]["category"] == "Entertainment: Film"

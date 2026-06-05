import httpx
import html
import random

BASE_URL = "https://opentdb.com/api.php"

class TriviaService:
    def __init__(self, base_url: str = BASE_URL):
        self.base_url = base_url

    async def fetch_trivia(self, category: int, amount: int, type: str):
        async with httpx.AsyncClient() as client:
            response = await client.get(self.base_url, params={"amount": amount, "type": type, "category": category})
            data = response.json()
            if data["response_code"] != 0:
                raise Exception("Failed to fetch trivia questions")
            
            processed_questions = []
            for question in data["results"]:

                correct_answer = html.unescape(question["correct_answer"])
                incorrect_answers = [html.unescape(ans) for ans in question["incorrect_answers"]]
                all_answers = incorrect_answers + [correct_answer]
                random.shuffle(all_answers)
                processed_question = {
                    "question": html.unescape(question["question"]),
                    "type": question["type"],
                    "difficulty": question["difficulty"],
                    "category": question["category"],
                    "correct_answer": correct_answer,
                    "all_answers": all_answers
                }
                processed_questions.append(processed_question)
            return processed_questions
        
    async def fetch_categories(self):
        async with httpx.AsyncClient() as client:
            response = await client.get("https://opentdb.com/api_category.php")
            data = response.json()
            return data["trivia_categories"]
        
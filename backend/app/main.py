from fastapi import FastAPI
import httpx
import uvicorn

app = FastAPI()
BASE_URL = "https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=multiple"


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/trivia")
async def get_trivia():
    print("Fetching trivia questions...")
    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL)
        response.raise_for_status()
        data = response.json()
        print(data)
        return data["results"]


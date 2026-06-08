from fastapi import FastAPI, HTTPException
from app.service import TriviaService
import httpx
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",  # VS Code Live Server common
        "http://localhost:5500",
        "http://127.0.0.1:8000",  # if same app serves frontend too
        "http://localhost:8000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    return FileResponse("app/templates/index.html")


@app.get("/quiz")
async def quiz(category: int, type: str, amount: int):
    return FileResponse("app/templates/quiz.html")


@app.get("/trivia")
async def get_trivia(category: int, type: str, amount: int):
    service = TriviaService()
    try:
        questions = await service.fetch_trivia(
            category=category, type=type, amount=amount
        )
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e))
    return questions


@app.get("/categories")
async def get_categories():
    service = TriviaService()
    categories = await service.fetch_categories()
    return categories

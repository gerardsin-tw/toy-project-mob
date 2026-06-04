from fastapi import FastAPI
from app.service import TriviaService
import httpx
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

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

@app.get("/")
async def root():
    return FileResponse("app/templates/index.html")

@app.get("/quiz")
async def quiz():
    return FileResponse("app/templates/quiz.html")

@app.get("/trivia")
async def get_trivia():
    service = TriviaService()
    questions = await service.fetch_trivia(amount=5)
    return questions



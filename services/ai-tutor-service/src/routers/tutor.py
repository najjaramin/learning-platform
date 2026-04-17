from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
import httpx, os

router = APIRouter()

OLLAMA_URL = os.getenv("OLLAMA_BASE_URL", "http://ollama:11434")
LLM_MODEL  = os.getenv("LLM_MODEL", "mistral")

class AskRequest(BaseModel):
    question:  str
    context:   Optional[str] = None
    course_id: Optional[str] = None

class QuizRequest(BaseModel):
    topic:         str
    num_questions: int = 5

async def call_llm(prompt: str) -> str:
    try:
        async with httpx.AsyncClient(timeout=60.0) as client:
            r = await client.post(f"{OLLAMA_URL}/api/generate",
                json={"model": LLM_MODEL, "prompt": prompt, "stream": False})
            return r.json().get("response", "Pas de réponse")
    except Exception as e:
        return f"Service IA indisponible : {str(e)}"

@router.post("/ask")
async def ask_question(req: AskRequest):
    ctx = f"\nContexte : {req.context}" if req.context else ""
    prompt = f"""Tu es un tuteur pédagogique.{ctx}
Question : {req.question}
Réponds clairement en français."""
    return {"question": req.question, "answer": await call_llm(prompt)}

@router.post("/quiz")
async def generate_quiz(req: QuizRequest):
    prompt = f"""Génère {req.num_questions} questions QCM sur : {req.topic}
Format :
Q: [question]
A) B) C) D) [options]
Réponse: [lettre]
En français uniquement."""
    return {"topic": req.topic, "quiz": await call_llm(prompt)}

@router.get("/recommendations/{user_id}")
async def get_recommendations(user_id: str):
    prompt = """Propose 5 sujets d'apprentissage pour un développeur web débutant.
Liste numérotée en français."""
    return {"user_id": user_id, "recommendations": await call_llm(prompt)}

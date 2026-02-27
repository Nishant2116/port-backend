"""
FastAPI Application — Portfolio Chatbot Backend
"""
import os
from dotenv import load_dotenv

# Load .env before anything else
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.chat import router as chat_router

app = FastAPI(
    title="Portfolio Chatbot API",
    description="AI chatbot backend for Nishant's portfolio, powered by Groq",
    version="1.0.0",
)

# CORS — allow portfolio frontend origins
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:3000",
    "http://127.0.0.1:5174",
    "http://127.0.0.1:5173",
    "https://nishant-portfolio-j9dwng1y0-nishant-deshmukhs-projects.vercel.app",
    "https://nishant2116.github.io",
]

app.add_middleware(
    CORSMiddleware,
    # When allow_credentials=True, you cannot use allow_origins=["*"]
    # So we either explicitly list origins, or for a public API allow all without credentials.
    allow_origins=["*"], 
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount routes
app.include_router(chat_router)


@app.get("/health")
async def health_check():
    """Health check endpoint for Railway deployment monitoring."""
    groq_key = os.getenv("GROQ_API_KEY", "")
    return {
        "status": "ok",
        "groq_configured": bool(groq_key and groq_key != "your_groq_api_key_here"),
    }

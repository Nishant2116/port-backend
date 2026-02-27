"""
Chat API routes
"""
from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from app.services.groq_service import stream_chat_response

router = APIRouter()


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: list[Message]


@router.post("/api/chat")
async def chat(request: ChatRequest):
    """
    Chat endpoint — accepts conversation history, returns streamed LLM response.
    Uses Server-Sent Events (SSE) for real-time token streaming.
    """
    try:
        messages = [{"role": m.role, "content": m.content} for m in request.messages]

        def generate():
            try:
                for token in stream_chat_response(messages):
                    # SSE format: data: <token>\n\n
                    yield f"data: {token}\n\n"
                yield "data: [DONE]\n\n"
            except Exception as e:
                yield f"data: [ERROR] {str(e)}\n\n"

        return StreamingResponse(
            generate(),
            media_type="text/event-stream",
            headers={
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "X-Accel-Buffering": "no",
            },
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

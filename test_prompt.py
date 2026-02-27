"""Quick test to verify Atom refuses math questions."""
from dotenv import load_dotenv
load_dotenv()

from app.services.groq_service import stream_chat_response

response = stream_chat_response([{"role": "user", "content": "What is 2+2?"}])
print("".join(response))

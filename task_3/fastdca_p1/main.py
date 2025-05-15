from fastapi import FastAPI, HTTPException, Depends
from Pydantic import BaseModel, Field
from datetime import datetime, UTC
from uuid import uuid4

# Initialize the FastAPI app
app = FastAPI(
    title="DACA Chatbot API",
    description="A FastApi-based API for a chatbot in the DACA tutorial; series",
    version="0.1.0",
)

# Complex pydantic models
class Metadata(BaseModel):
    timestamp: datetime = Field(default_factory=lambda: datetime.now(tz=UTC))
    session_id: str = Field(default_factory=lambda: str(uuid4))

class Message(BaseModel):
    user_id: str
    text: str
    metadata: Metadata
    tags: list[str] | None = None # Optional list of tags

class Response(BaseModel):
    user_id: str
    reply: str
    metadata: Metadata

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "Welcome to tha DCA chatbot API! Access / docs for the API documentation."
    }

# GET endpoint with query parameters
@app.get("/users/{user_id}")
async def get_user(user_id: str, role: str | None = None):
    user_info = {"user_id": user_id, "role": role if role else "guest"}

# POST endpoint for chatting
@app.post("/chat/", response_model=Response)
async def chat(message: Message):
    if not message.text.strip():
        raise HTTPException(
            status_code=400, detail="Message text cannot be empty"
        )
    reply_text = f"Hello, {message.user_id}! You said: '{message.text}'. How can I assist you today?"
    return Response(
        user_id=message.user_id,
        reply=reply_text,
        metadata=Metadata() # Auto_generate timestamp and sessiom_id
    )
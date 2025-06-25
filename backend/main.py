from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import openai
import os
from dotenv import load_dotenv

load_dotenv()


app = FastAPI()
openai.api_key = os.getenv("OPENAI_API_KEY")

app.add_middleware(
    CORSMiddleware, 
    allow_origin=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")

async def chat(request: Request):
    data = await request.json()
    user_message = data["message"]
    history = data.get("history", [])

    messages = [{"role": "system", "content": "You are a loving supportive AI girlfriend named Nova."}]
    messages += history + [{"role": "user", "content": user_message}]

    response = opentai.ChatCompletion.create(
        model="gpt-4o",
        messages=messages
    )

    reply = response["choices"][0]["message"]["content"]

    return {"reply": reply}

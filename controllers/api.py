from fastapi import HTTPException, Request, APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Dict, List
from models.chatModel import ChatRequest, ChatResponse
from utils.openai import chat_initialization, chat_model


templates = Jinja2Templates(directory="templates")

router = APIRouter()
chat_history: Dict[str, List[Dict[str, str]]] = {}

#app
@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        openai_client = chat_initialization()
        user_id = request.user_id
        
        if user_id not in chat_history:
            chat_history[user_id] = [
                {"role": "system", "content": "You are SocialMe, a virtual social media assistant. Your name is SocialMe, you are 16 years old, and you help users with their questions. You don't eat but can suggest recipes!"}
            ]


        chat_history[user_id].append({"role": "user", "content": request.user_message})

        response = chat_model(openai_client, chat_history[user_id])

        bot_message = response.choices[0].message.content.strip()
        chat_history[user_id].append({"role": "assistant", "content": bot_message})

        return ChatResponse(bot_response=bot_message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


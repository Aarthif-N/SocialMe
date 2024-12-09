import openai
from dotenv import load_dotenv
import os
from models.openaiModel import OpenAIRequest

load_dotenv()


def chat_initialization():
    #Chat Initialization
    OPENAI_API_KEY = os.getenv('OPENAI_KEY')
    if not OPENAI_API_KEY:
        raise ValueError("OpenAI API key is not set in the environment variables.")
    openai.api_key = OPENAI_API_KEY
    return openai


def chat_model(openai, message: OpenAIRequest):
    return openai.chat.completions.create(model="gpt-3.5-turbo", messages=message)

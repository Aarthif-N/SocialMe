from pydantic import BaseModel
import openai

class OpenAIRequest(BaseModel):
    message: str
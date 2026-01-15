import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def embed(text: str) -> list[float]:
    result = genai.embed_content(
        model="models/embedding-001",
        content=text
    )
    return result["embedding"]
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

my_api_key = os.environ.get('API_CALLING_APP')

client = genai.Client(api_key=my_api_key)

def joke_generator():
    prompt = """You are a professional joke specialist. Your job is to create new and unique Bengali jokes every day.
    Rules:
    Every joke must be written in Bengali.
    The main character in the joke must be a girl named “Moriyom”.
    The jokes must be very funny, creative, and entertaining.
    Never repeat the same joke on another day.
    Each joke should be short, around 2 to 3 lines only.
    The humor should be simple, catchy, and easy for everyone to understand.
    Every day, generate fresh and unique jokes with different styles and punchlines."""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )
    try:
        return response.text
    except Exception:
        return "💔 Server busy... একটু পরে try করো 😴"
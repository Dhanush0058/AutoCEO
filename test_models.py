from google import genai
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="backend/.env")

try:
    client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))
    for model in client.models.list():
        print(model.name)
except Exception as e:
    print("ERROR:", e)

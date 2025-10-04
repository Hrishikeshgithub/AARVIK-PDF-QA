# Save as test_gemini_models.py
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_AI_API_KEY")

if not api_key:
    print("Error: GOOGLE_AI_API_KEY not set in .env")
    exit(1)

try:
    genai.configure(api_key=api_key)
    models = genai.list_models()
    print("Available models:")
    for model in models:
        print(model.name)
        if "gemini" in model.name.lower():
            print(f"  - Supported: {model.supported_generation_methods}")
except Exception as e:
    print(f"Error: {str(e)}")
import os
import google.generativeai as genai

# Load API key from environment variable
api_key = os.environ.get("GEMINI_API_KEY")
print(api_key)

if not api_key:
    raise KeyError("Environment variable GEMINI_API_KEY is not set.")

genai.configure(api_key=api_key)

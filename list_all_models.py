import os
from google import genai

# Setup API Key securely
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("Error: GEMINI_API_KEY environment variable not set.")
    exit(1)

client = genai.Client(api_key=api_key)

print("Listing ALL available models:")
for model in client.models.list():
    print(f"Name: {model.name}")

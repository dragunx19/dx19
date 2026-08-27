import os
from google import genai
from google.genai import types

# Setup API Key securely
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("Error: GEMINI_API_KEY environment variable not set.")
    exit(1)

client = genai.Client(api_key=api_key)

# Setup prompt
prompt = "3D chrome metal logo 'X19' standing majestically in the frozen waters of Greenland. Hyper-realistic landscape with large glaciers, snow-capped mountains, cloudy sky, and perfect mirror reflection on the icy water surface."

print(f"Generating image with prompt: {prompt}")

try:
    # Use generate_content for image models as recommended
    response = client.models.generate_content(
        model='gemini-3.1-flash-image',
        contents=prompt,
        config=types.GenerateContentConfig(
            # Assuming aspect ratio configuration might need to be passed differently or if supported by the model config
        )
    )

    # Note: Accessing generated image from generate_content might differ
    print(f"Content generated: {response.text}")

except Exception as e:
    print(f"An error occurred: {e}")

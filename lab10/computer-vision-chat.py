from openai import OpenAI
import dotenv
import os

dotenv.load_dotenv()

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment_name = os.getenv("MODEL_ID")
api_key = os.getenv("APIKEY")

client = OpenAI(base_url=endpoint, api_key=api_key)

response = client.responses.create(
    model=deployment_name,
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "what's in this image?"},
                {
                    "type": "input_image",
                    "image_url": "https://microsoftlearning.github.io/mslearn-ai-fundamentals/data/joystick.png",
                },
            ],
        }
    ],
)

print(f"answer: {response.output_text}")

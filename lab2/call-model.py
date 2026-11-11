import os
from pathlib import Path

from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import OpenAI


load_dotenv(Path(__file__).parents[1] / ".env")

project_endpoint = os.environ["PROJECT_ENDPOINT"].rstrip("/")
deployment = os.environ["MODEL_ID"]

client = OpenAI(
    base_url=f"{project_endpoint}/openai/v1/",
    api_key=get_bearer_token_provider(
        DefaultAzureCredential(), "https://ai.azure.com/.default"
    ),
)

response = client.chat.completions.create(
    model=deployment,
    messages=[{"role": "user", "content": "Say hello in one short sentence."}],
)

print(response.choices[0].message.content)
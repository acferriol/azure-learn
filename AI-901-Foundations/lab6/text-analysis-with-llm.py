from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
import os
import dotenv

dotenv.load_dotenv()

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment_name = os.getenv("MODEL_ID")
api_key = os.getenv("APIKEY")

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://ai.azure.com/.default"
)

task = """Summarize this review as a single short paragraph:

Commodore 64: A Strong Contender in the Home Computer Market

Commodore's long-awaited Commodore 64 has finally arrived on dealers' shelves, and first impressions suggest that the company may have another substantial success on its hands. Priced aggressively and boasting a full 64K of RAM, the machine offers specifications that would have seemed remarkable in a home computer only a short time ago. Its colourful graphics and impressive sound capabilities place it among the most capable entertainment-oriented systems currently available.

Particularly noteworthy is the SID sound generator, which produces effects and musical output far beyond what users have come to expect from machines in this price bracket. Software houses are already expressing strong interest in the platform, and the combination of advanced graphics and sound should make the Commodore 64 an attractive proposition for both game developers and serious hobbyists alike.

The machine is not without its shortcomings, however. The keyboard, while serviceable, lacks the solid feel of some competing systems, and Commodore's documentation will do little to reassure newcomers to computing. Furthermore, prospective purchasers may wish to consider the total cost of ownership, as disk drives and other peripherals remain relatively expensive. Nevertheless, the Commodore 64 enters the market as one of the most compelling home computers currently available and is likely to be a significant force in the months ahead."""

client = OpenAI(base_url=endpoint, api_key=token_provider)

response = client.responses.create(
    model=deployment_name,
    instructions="You are an AI assistant that analyzes and summarizes text.",
    input=task,
)

print(f"answer: {response.output_text}")

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import dotenv
import os

dotenv.load_dotenv()
apikey = os.getenv("LANGUAGE_APIKEY")

credential = AzureKeyCredential(apikey)
client = TextAnalyticsClient(
    endpoint=os.getenv("LANGUAGE_ENDPOINT"),
    credential=credential,
)

documents = [
    "I had the best day of my life.",
    "This was a waste of my time. The speaker put me to sleep.",
    "No tengo dinero ni nada que dar...",
]
result = client.detect_language(documents=documents)
print(result)

result = client.analyze_sentiment(documents=documents)
print(result)

result = client.recognize_entities(documents=documents)
print(result)

result = client.recognize_pii_entities(documents=documents)
print(result)

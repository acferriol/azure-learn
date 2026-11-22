import base64
import requests
from azure.identity import AzureCliCredential

credential = AzureCliCredential()
token = credential.get_token("https://ai.azure.com/.default").token

url = (
    "https://ai-concepts-course-resource.services.ai.azure.com/"
    "managed-deployments/prompthero--openjourney/"
    "v1/images/generations"
)

payload = {
    "model": "prompthero--openjourney",
    "prompt": "mdjrny-v4 style, a cute baby sea otter",
    "response_format": "b64_json",
    "size": "512x512",
    "n": 1,
}

response = requests.post(
    url,
    headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
    json=payload,
    timeout=300,
)

print("STATUS:", response.status_code)

if response.status_code != 200:
    print("ERROR DE AZURE:")
    print(response.text[:4000])
    print("REQUEST ID:", response.headers.get("x-ms-request-id"))
    print("APIM REQUEST ID:", response.headers.get("apim-request-id"))
    raise SystemExit(1)

result = response.json()
image_base64 = result["data"][0]["b64_json"]

with open("otter.png", "wb") as f:
    f.write(base64.b64decode(image_base64))

print("Imagen generada: otter.png")

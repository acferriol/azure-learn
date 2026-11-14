# Azure for Student restrict use, only sample

import sys
import json

from azure.ai.contentunderstanding import ContentUnderstandingClient
from azure.ai.contentunderstanding.models import AnalysisInput, AnalysisResult
from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import AzureError
from azure.identity import DefaultAzureCredential


def main() -> None:
    # Insert the following configurations.
    # 1) AZURE_CONTENT_UNDERSTANDING_ENDPOINT - the endpoint to your Content Understanding resource.
    endpoint = "https://content-project-resource.services.ai.azure.com/"

    # 2) CONTENT_UNDERSTANDING_KEY - your Content Understanding API key (optional if using DefaultAzureCredential).
    key = ""

    # 3) FILE_URL - you can replace this with your own URL.
    file_url = ""

    # ANALYZER_ID - the ID of the analyzer to use.
    analyzer_id = "prebuilt-receipt"

    # API_VERSION - the API version to use.
    api_version = "2025-11-01"

    # Set up Content Understanding client.
    credential = (
        AzureKeyCredential(key) if key and "" not in key else DefaultAzureCredential()
    )
    client = ContentUnderstandingClient(
        endpoint=endpoint, credential=credential, api_version=api_version
    )

    # [START analyze]
    print(f"Analyzing with {analyzer_id} analyzer...")
    print(f"  File URL: {file_url}\n")

    try:
        poller = client.begin_analyze(
            analyzer_id=analyzer_id,
            inputs=[AnalysisInput(url=file_url)],
        )
        result: AnalysisResult = poller.result()
    except AzureError as err:
        print(f"[Azure Error]: {err.message}")
        sys.exit(1)
    except Exception as ex:
        print(f"[Unexpected Error]: {ex}")
        sys.exit(1)
    # [END analyze]

    # [START output_result]
    print("=" * 50)
    print("Analysis result:")
    print("=" * 50 + "\n")

    max_display_lines = 50
    result_str = json.dumps(result.as_dict(), indent=2)
    ret_lines = result_str.splitlines()

    if len(ret_lines) > max_display_lines:
        print("\n".join(ret_lines[:max_display_lines]))
        print(
            f"\n {len(ret_lines) - max_display_lines} more lines to be displayed...\n"
        )
    else:
        print(result_str)
    # [END output_result]


if __name__ == "__main__":
    main()

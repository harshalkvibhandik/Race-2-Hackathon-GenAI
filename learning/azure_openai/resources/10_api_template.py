#Note: The openai-python library support for Azure OpenAI is in preview.
import json
import os
from openai import AzureOpenAI

openai.api_type = "azure"
openai.api_base = "https://hsbc-aiml-team-resource.openai.azure.com/"
openai.api_version = "2023-06-01-preview"
openai.api_key = os.getenv("OPENAI_API_KEY")

client = AzureOpenAI(
    azure_endpoint="https://hsbc-aiml-team-resource.openai.azure.com/",
    api_version="2023-07-01-preview",
    api_key=os.environ["OPENAI_API_KEY"]
)

result = client.images.generate(
    model="DALL-E-3",
    prompt='programmer coding on the moon',
    size='1024x1024',
    n=1
)

image_url = json.loads(result.model_dump_json())["data"][0]["url"]
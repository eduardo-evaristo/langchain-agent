import requests
import json
import os
from langchain.agents import Tool
from dotenv import load_dotenv

load_dotenv()

url = "https://google.serper.dev/search"


def browse(query):
    payload = json.dumps(
        {
            "q": query,
            "hl": "pt-br",
        }
    )

    headers = {
        "X-API-KEY": os.environ["SERPER_DEV_API_KEY"],
        "Content-Type": "application/json",
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


browse_text = Tool(
    func=browse,
    description="This tool searches the web based on a given query",
    name="browse_text",
)

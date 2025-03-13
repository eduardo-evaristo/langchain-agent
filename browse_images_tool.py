from duckduckgo_search import DDGS
from langchain.agents import Tool

# This is our searching engine, this is the object that interacts with duckduckgo
ddgs = DDGS()

def browse(query):
    return ddgs.images(query, max_results=2)

browse_images = Tool(func=browse, description='This tool searches the web for images based on a given query', name='browse_images')

from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

if 'GOOGLE_API_KEY'  not in os.environ:
    print('You must provide an API key')
    exit(1)

# This is our LLM model, in this case, Gemini
llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash', temperature=0)

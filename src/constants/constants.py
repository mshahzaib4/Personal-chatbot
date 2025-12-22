import os
from dotenv import load_dotenv
from pinecone import Pinecone
load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not PINECONE_API_KEY:
    raise ValueError("PINECONE_API_KEY is missing")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is missing")

PC = Pinecone(api_key=PINECONE_API_KEY)

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY

INDEX_NAME = "chatbot"


import os
from dotenv import load_dotenv

load_dotenv()

# LangSmith entegrasyonu için gerekli.
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# OpenAI API anahtarı
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

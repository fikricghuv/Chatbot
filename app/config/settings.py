# import os
# from dotenv import load_dotenv

# load_dotenv()

# class Settings:
#     OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
#     LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
#     LANGCHAIN_PROJECT = os.getenv("LANGCHAIN_PROJECT")
#     LANGCHAIN_TRACING_V2 = "true"

# settings = Settings()

from pydantic import BaseSettings
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    LANGCHAIN_API_KEY: str
    LANGCHAIN_TRACING_V2: str
    LANGCHAIN_PROJECT: str

    class Config:
        env_file = ".env"  # File .env di root project

settings = Settings()


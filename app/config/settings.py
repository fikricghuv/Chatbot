from pydantic_settings import BaseSettings
# from dotenv import load_dotenv

# Load environment variables from .env file
# load_dotenv()

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    LANGCHAIN_API_KEY: str
    LANGCHAIN_TRACING_V2: str
    LANGCHAIN_PROJECT: str
    LANGCHAIN_ENDPOINT: str

    class Config:
        env_file = ".env"

settings = Settings()


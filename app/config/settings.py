from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    LANGCHAIN_API_KEY: str
    LANGCHAIN_TRACING_V2: str
    LANGCHAIN_PROJECT: str
    LANGCHAIN_ENDPOINT: str
    DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()


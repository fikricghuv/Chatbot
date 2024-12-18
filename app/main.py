from fastapi import FastAPI
from app.routes.ask_routes import router
from app.config.settings import settings
import os

# Set environment variables
os.environ["OPENAI_API_KEY"] = settings.OPENAI_API_KEY
os.environ["LANGCHAIN_API_KEY"] = settings.LANGCHAIN_API_KEY
os.environ["LANGCHAIN_TRACING_V2"] = settings.LANGCHAIN_TRACING_V2
os.environ["LANGCHAIN_PROJECT"] = settings.LANGCHAIN_PROJECT

# Initialize FastAPI app
app = FastAPI(
    title="BRI Insurance Chatbot API",
    description="API untuk melayani pertanyaan seputar produk asuransi BRI INSURANCE",
    version="1.0.0"
)

@app.on_event("startup")
async def startup_event():
    print("Application startup: All systems ready!")

@app.on_event("shutdown")
async def shutdown_event():
    print("Application shutdown: Cleaning resources!")

# Register routes
app.include_router(router, prefix="/api", tags=["ask","home"])

@app.get("/home")
def main_root():
    return {"message": "Welcome to the Chatbot App"}

# Run FastAPI server (optional untuk debugging lokal)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)



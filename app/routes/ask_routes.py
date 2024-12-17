from fastapi import APIRouter, HTTPException
from app.model.query_model import QueryRequest
from app.controller.ask_controller import handle_question
import logging

router = APIRouter()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@router.get("/")
def root():
    return {"message": "API is running!"}

@router.post("/ask")
async def ask_question(query: QueryRequest):
    try:
        logger.info(f"Received question: {query.question}")
        answer = handle_question(query.question)
        logger.info(f"Answer: {answer}")
        return {"question": query.question, "answer": answer}
    except Exception as e:
        logger.error(f"Error occurred: {e}")
        raise HTTPException(status_code=500, detail=str(e))

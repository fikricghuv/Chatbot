from fastapi import APIRouter, HTTPException
from app.model.query_model import QueryRequest, QueryHistory
from app.controller.ask_controller import handle_question
import logging
import os
from app.config.settings import settings
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

router = APIRouter()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

os.environ["DATABASE_URL"] = settings.DATABASE_URL
engine = create_async_engine(os.environ["DATABASE_URL"], echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

@router.post("/ask")
async def ask_question(query: QueryRequest):
    """
    Endpoint untuk menjawab pertanyaan pengguna terkait produk asuransi BRI INSURANCE.
    """
    async with async_session() as session:
        try:
            user_input = query.question
            if not user_input:
                raise HTTPException(status_code=400, detail="Pertanyaan tidak boleh kosong.")
            else:
                logger.info(f"Received question: {query.question}")
                answer = handle_question(query.question)
                logger.info(f"Answer: {answer}")

                # Simpan data ke database
                history_entry = QueryHistory(question=user_input, answer=answer)
                session.add(history_entry)
                await session.commit()

            return {"question": query.question, "answer": answer}
        except Exception as e:
            logger.error(f"Error occurred: {e}")
            raise HTTPException(status_code=500, detail=str(e))
        finally:
                await session.close()

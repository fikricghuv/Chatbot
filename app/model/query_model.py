from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class QueryRequest(BaseModel):
    question: str

# Model untuk tabel histori
class QueryHistory(Base):
    __tablename__ = "query_history"
    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, nullable=False)
    answer = Column(Text, nullable=False)
from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base
from datetime import datetime


class SnippetModel(Base):
    __tablename__ = "snippets"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    code = Column(String, nullable=False)
    explanation = Column(String)
    difficulty = Column(String)
    category = Column(String)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

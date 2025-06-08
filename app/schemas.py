from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class SnippetSchema(BaseModel):
    id: int
    title: str
    code: str
    explanation: str
    category: Optional[str] = None
    difficulty: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class SnippetCreate(BaseModel):
    title: str
    code: str
    explanation: str
    category: Optional[str] = None
    difficulty: Optional[str] = None

    class Config:
        from_attributes = True


class SnippetUpdate(BaseModel):
    title: Optional[str] = None
    code: Optional[str] = None
    explanation: Optional[str] = None
    category: Optional[str] = None
    difficulty: Optional[str] = None

    class Config:
        from_attributes = True

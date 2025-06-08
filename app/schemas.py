from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum


class DifficultyEnum(str, Enum):
    beginner = "beginner"
    intermediate = "intermediate"
    advanced = "advanced"


class SnippetSchema(BaseModel):
    id: int
    title: str = Field(..., example="Read a File", description="Human-readable snippet title")
    code: str = Field(..., example="with open('file.txt') as f:\n    data = f.read()", description="The Python code snippet")
    explanation: str = Field(..., example="Reads the contents of a file into a string.", description="Explanation of what the code does")
    category: Optional[str] = Field(None, example="File I/O", description="Snippet category")
    difficulty: Optional[DifficultyEnum] = Field(None, example="beginner", description="Snippet difficulty level")
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class SnippetCreate(BaseModel):
    title: str
    code: str
    explanation: str
    category: Optional[str] = None
    difficulty: Optional[DifficultyEnum] = None

    class Config:
        from_attributes = True


class SnippetUpdate(BaseModel):
    title: Optional[str] = None
    code: Optional[str] = None
    explanation: Optional[str] = None
    category: Optional[str] = None
    difficulty: Optional[DifficultyEnum] = None

    class Config:
        from_attributes = True

from pydantic import BaseModel, Field
from typing import List, Literal


class SnippetModel(BaseModel):
    title: str
    code: str
    explanation: str
    difficulty: Literal["beginner", "intermediate", "advanced"]
    related: List[str] = Field(default_factory=list)
    category: str

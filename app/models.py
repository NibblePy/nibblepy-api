from pydantic import BaseModel
from typing import List


class SnippetResponse(BaseModel):
    title: str
    code: str
    explanation: str
    difficulty: str
    related: List[str]
    category: str

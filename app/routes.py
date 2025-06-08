from fastapi import HTTPException, Query, APIRouter, Depends
from typing import Optional, List
from sqlalchemy.orm import Session
from sqlalchemy import or_
from enum import Enum

from app.database import get_db
from app.models import SnippetModel
from app.schemas import SnippetSchema, DifficultyEnum
from pydantic import BaseModel

router = APIRouter()


# --- RESPONSE ENVELOPES ---

class SnippetListResponse(BaseModel):
    results: List[SnippetSchema]
    count: int


class CategoriesResponse(BaseModel):
    categories: List[str]


class DifficultiesResponse(BaseModel):
    difficulties: List[str]


class HealthResponse(BaseModel):
    status: str = "ok"


# --- ROUTES ---

@router.get("/snippet", response_model=SnippetSchema, tags=["Snippets"])
def read_snippet(
    topic: str = Query(..., description="Topic of the snippet"),
    db: Session = Depends(get_db)
):
    """
    GET code snippet by topic (title)
    Example: /snippet?topic=Read a File
    """
    normalized_topic = topic.strip()
    snippet = db.query(SnippetModel).filter(SnippetModel.title.ilike(normalized_topic)).first()
    if snippet:
        return snippet
    raise HTTPException(status_code=404, detail="Snippet not found")


@router.get("/snippets", response_model=SnippetListResponse, tags=["Snippets"])
def get_snippets(
    difficulty: Optional[DifficultyEnum] = Query(None, description="Filter by difficulty"),
    category: Optional[str] = Query(None, description="Filter by category"),
    limit: int = Query(20, ge=1, le=100, description="Number of snippets to return"),
    offset: int = Query(0, ge=0, description="Offset for pagination"),
    db: Session = Depends(get_db)
):
    """
    List snippets with optional filtering and pagination.
    """
    query = db.query(SnippetModel)

    if category:
        query = query.filter(SnippetModel.category.ilike(category))
    if difficulty:
        query = query.filter(SnippetModel.difficulty == difficulty.value)

    total = query.count()
    snippets = query.offset(offset).limit(limit).all()
    return SnippetListResponse(results=snippets, count=total)


@router.get("/snippets/search", response_model=SnippetListResponse, tags=["Snippets"])
def search_snippets(
    query: str = Query(..., min_length=1, description="Search query string"),
    limit: int = Query(20, ge=1, le=100, description="Number of snippets to return"),
    offset: int = Query(0, ge=0, description="Offset for pagination"),
    db: Session = Depends(get_db)
):
    """
    Search in title, code, and explanation.
    """
    query_lower = f"%{query.lower()}%"
    results_query = db.query(SnippetModel).filter(
        or_(
            SnippetModel.title.ilike(query_lower),
            SnippetModel.code.ilike(query_lower),
            SnippetModel.explanation.ilike(query_lower)
        )
    )
    total = results_query.count()
    results = results_query.offset(offset).limit(limit).all()
    return SnippetListResponse(results=results, count=total)


@router.get("/categories", response_model=CategoriesResponse, tags=["Metadata"])
def list_categories(db: Session = Depends(get_db)):
    """
    GET a list of all available categories.
    """
    categories = db.query(SnippetModel.category).distinct().all()
    cat_list = sorted({c[0] or "Uncategorized" for c in categories})
    return CategoriesResponse(categories=cat_list)


@router.get("/difficulties", response_model=DifficultiesResponse, tags=["Metadata"])
def list_difficulties(db: Session = Depends(get_db)):
    """
    GET a list of all available difficulty levels.
    """
    difficulties = db.query(SnippetModel.difficulty).distinct().all()
    diff_list = sorted({d[0] for d in difficulties if d[0]})
    return DifficultiesResponse(difficulties=diff_list)


@router.api_route("/health", methods=["GET", "HEAD"], response_model=HealthResponse, tags=["Utils"])
def check_api_health():
    """
    Health check endpoint.
    """
    return HealthResponse()

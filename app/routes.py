from fastapi import HTTPException, Query, APIRouter, Depends
from typing import Optional, List
from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.database import get_db
from app.models import SnippetModel
from app.schemas import SnippetSchema

router = APIRouter()


@router.get("/snippet", response_model=SnippetSchema, tags=["Snippets"])
def read_snippet(topic: str = Query(..., description="Topic of the snippet"), db: Session = Depends(get_db)):
    """
    GET code snippet by topic (title)
    Example: /snippet?topic=dictionaries
    """
    snippet = db.query(SnippetModel).filter(SnippetModel.title.ilike(topic)).first()
    if snippet:
        return snippet
    raise HTTPException(status_code=404, detail="Snippet not found")


@router.get("/snippets", response_model=List[SnippetSchema], tags=["Snippets"])
def get_snippets(
    difficulty: Optional[str] = Query(None, description="Filter by difficulty"),
    category: Optional[str] = Query(None, description="Filter by category"),
    db: Session = Depends(get_db)
):
    query = db.query(SnippetModel)

    if category:
        query = query.filter(SnippetModel.category.ilike(category))
    if difficulty:
        query = query.filter(SnippetModel.difficulty.ilike(difficulty))

    return query.all()


@router.get("/snippets/search", tags=["Snippets"])
def search_snippets(
    query: str = Query(..., min_length=1, description="Search query string"),
    db: Session = Depends(get_db)
):
    """Search in title, code, and explanation"""
    query_lower = f"%{query.lower()}%"
    results = db.query(SnippetModel).filter(
        or_(
            SnippetModel.title.ilike(query_lower),
            SnippetModel.code.ilike(query_lower),
            SnippetModel.explanation.ilike(query_lower)
        )
    ).all()
    return {"results": results, "count": len(results)}


@router.get("/categories", tags=["Metadata"])
def list_categories(db: Session = Depends(get_db)):
    """GET a list of all available categories"""
    categories = db.query(SnippetModel.category).distinct().all()
    return {"categories": sorted({c[0] or "Uncategorized" for c in categories})}


@router.get("/difficulties", tags=["Metadata"])
def list_difficulties(db: Session = Depends(get_db)):
    """GET a list of all available difficulty levels"""
    difficulties = db.query(SnippetModel.difficulty).distinct().all()
    return {"difficulties": sorted({d[0] for d in difficulties})}


@router.api_route("/health", methods=["GET", "HEAD"], tags=["Utils"])
def check_api_health():
    return {"status": "ok"}

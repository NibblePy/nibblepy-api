from fastapi import HTTPException, Query, APIRouter
from typing import Optional
from app.utils import get_snippets_by_topic, fetch_all_snippets
from app.models import SnippetResponse

router = APIRouter()


@router.get("/snippet", response_model=SnippetResponse)
def read_snippet(topic: str = Query(..., description="Topic of the snippet")):
    """Fetch code snippet for the given topic"""
    snippet = get_snippets_by_topic(topic)
    if snippet:
        return snippet
    raise HTTPException(status_code=404, detail="Snippet not found")


@router.get("/snippets")
def get_snippets(
    difficulty: Optional[str] = Query(None, description="Filter by difficulty: beginner, intermediate, advanced"),
    category: Optional[str] = Query(None, description="Filter by category (e.g. data types, loops, etc.)")
):
    """Fetch all snippets and filter by difficulty or category"""
    snippets = fetch_all_snippets()
    filtered = {}

    for key, snippet in snippets.items():
        if difficulty and snippet.get("difficulty", "").lower() != difficulty.lower():
            continue
        if category and snippet.get("category", "").lower() != category.lower():
            continue

        filtered[key] = snippet

    return filtered


@router.get("/categories", tags=["Metadata"])
def list_categories():
    """Return a list of all available categories"""
    snippets = fetch_all_snippets()
    categories = sorted({s.get("category", "Uncategorized") for s in snippets.values()})
    return {"categories": categories}


@router.get("/difficulties", tags=["Metadata"])
def list_difficulties():
    """Return a list of all available difficulty levels"""
    snippets = fetch_all_snippets()
    difficulties = sorted({s.get("difficulty", "unknown") for s in snippets.values()})
    return {"difficulties": difficulties}


@router.get("/health")
def check_api_health():
    return {"ok": True}

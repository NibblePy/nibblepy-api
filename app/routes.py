from fastapi import HTTPException, Query, APIRouter
from typing import Optional, List
from app.utils import get_snippet_by_topic, load_all_snippets
from app.models import SnippetModel

router = APIRouter()
snippets = load_all_snippets()


@router.get("/snippet", response_model=SnippetModel, tags=["Snippets"])
def read_snippet(topic: str = Query(..., description="Topic of the snippet")):
    """
    GET code snippet for the given snippet title
    Example: /snippet?topic=dictionaries
    """
    snippet = get_snippet_by_topic(topic)
    if snippet:
        return snippet
    raise HTTPException(status_code=404, detail="Snippet not found")


@router.get("/snippets", tags=["Snippets"])
def get_snippets(
    difficulty: Optional[str] = Query(None, description="Filter by difficulty: beginner, intermediate, advanced"),
    category: Optional[str] = Query(None, description="Filter by category (e.g. data types, loops, etc.)")
):
    """GET all snippets and filter by difficulty or category"""
    filtered = {}

    for key, snippet in snippets.items():
        if difficulty and snippet.difficulty.lower() != difficulty.lower():
            continue
        if category and snippet.category != category.lower():
            continue

        filtered[key] = snippet

    return filtered


@router.get("/categories", tags=["Metadata"])
def list_categories():
    """GET a list of all available categories"""
    categories = sorted({s.category or "Uncategorized" for s in snippets.values()})
    return {"categories": categories}


@router.get("/difficulties", tags=["Metadata"])
def list_difficulties():
    """GET a list of all available difficulty levels"""
    difficulties = sorted({s.difficulty or "Uncategorized" for s in snippets.values()})
    return {"difficulties": difficulties}


@router.get("/snippets/search", tags=["Snippets"])
def search_snippets(query: str = Query(..., min_length=1, description="Search query string")):
    """
    GET snippets matching the query
    Example: /snippets/search?query=list
    """
    query_lower = query.lower()
    results = []

    for key, snippet in snippets.items():
        if (
            query_lower in snippet.title.lower()
            or query_lower in snippet.code.lower()
            or query_lower in snippet.explanation.lower()
        ):
            results.append({**snippet.dict(), "id": key})

    return {"results": results, "count": len(results)}


@router.get("/snippets", tags=["Snippets"])
def filter_snippets(
    category: Optional[str] = Query(None, description="Category name"),
    difficulty: Optional[str] = Query(None, description="Difficulty level"),
    related: Optional[List[str]] = Query(None, description="Related concept(s)")
):
    results = []

    for key, snippet in snippets.items():
        if category and snippet.category.lower() != category.lower():
            continue
        if difficulty and snippet.difficulty.lower() != difficulty.lower():
            continue
        if related:
            if not any(rel.lower() in [r.lower() for r in snippet.related] for rel in related):
                continue

        results.append({**snippet, "id": key})

    return {"results": results, "count": len(results)}


@router.api_route("/health", methods=["GET", "HEAD"], tags=["Utils"])
def check_api_health():
    return {"status": "ok"}

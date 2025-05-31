from fastapi import FastAPI, HTTPException, Query
from app.db import get_snippets_by_topic
from app.models import SnippetResponse

app = FastAPI(title="NibblePy API", version="1.0")


@app.get("/snippet", response_model=SnippetResponse)
def read_snippet(topic: str = Query(..., description="Topic of the snippet")):
    """Fetch code snippet for the given topic"""
    snippet = get_snippets_by_topic(topic)
    if snippet:
        return snippet
    raise HTTPException(status_code=404, detail="Snippet not found")

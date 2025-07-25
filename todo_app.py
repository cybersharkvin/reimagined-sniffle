from typing import TypedDict, Literal, Annotated, Optional
from datetime import date

class Todo(TypedDict):
    id: int
    title: str
    priority: Literal['low', 'medium', 'high']
    due: Optional[date]


def add_todo(item: Todo) -> Annotated[str, 'UUID']:
    """Create a new TODO and return its unique identifier (RFC 4122)."""
    pass

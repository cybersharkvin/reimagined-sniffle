from __future__ import annotations
import inspect
import typing as t
from datetime import date

# Step 2: structured spec extraction

def extract_spec(func: t.Callable) -> dict:
    sig = inspect.signature(func)
    hints = t.get_type_hints(func)
    doc = inspect.getdoc(func) or ""
    return {
        "name": func.__name__,
        "params": {k: hints.get(k, object) for k in sig.parameters},
        "returns": hints.get("return", object),
        "doc": doc,
    }

# Step 4: assemble grammar for add_todo

def build_grammar(func: t.Callable) -> str:
    spec = extract_spec(func)
    assert spec["name"] == "add_todo"
    grammar = """
start: call
call: "{" ITEM ":" todo "}"
todo: "{" ID ":" NUMBER "," TITLE ":" STRING "," PRIORITY_KEY ":" PRIORITY "," DUE ":" (DATE | "null") "}"
ITEM: "\\\"item\\\""
ID: "\\\"id\\\""
TITLE: "\\\"title\\\""
PRIORITY_KEY: "\\\"priority\\\""
DUE: "\\\"due\\\""
PRIORITY: "\\\"low\\\"" | "\\\"medium\\\"" | "\\\"high\\\""
DATE: /"\d{4}-\d{2}-\d{2}"/
STRING: ESCAPED_STRING
NUMBER: /-?\d+/
%import common.ESCAPED_STRING
%import common.WS
%ignore WS
"""
    return grammar.strip()

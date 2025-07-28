import json
from datetime import date
from hypothesis import given, strategies as st
from lark import Lark
from util import gbnf_to_lark

with open('todo.gbnf') as f:
    GRAMMAR = f.read()

parser = Lark(gbnf_to_lark(GRAMMAR), start='start')

todo_strategy = st.builds(
    lambda id, title, priority, due: {"item": {"id": id, "title": title, "priority": priority, "due": due}},
    id=st.integers(min_value=0, max_value=1000),
    title=st.text(min_size=1, max_size=10),
    priority=st.sampled_from(["low", "medium", "high"]),
    due=st.one_of(st.none(), st.dates().map(lambda d: d.isoformat())),
)

@given(todo_strategy)
def test_fuzz(todo):
    payload = json.dumps(todo)
    parser.parse(payload)

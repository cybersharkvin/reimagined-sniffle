from pathlib import Path
from todo_app import add_todo
from grammar_tools import build_grammar

if __name__ == '__main__':
    gbnf = build_grammar(add_todo)
    Path('todo.gbnf').write_text(gbnf)
    print(gbnf)

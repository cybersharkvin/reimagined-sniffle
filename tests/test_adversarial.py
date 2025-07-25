from lark import Lark, exceptions
from util import gbnf_to_lark

with open('todo.gbnf') as f:
    GRAMMAR = f.read()

parser = Lark(gbnf_to_lark(GRAMMAR), start='start')

def test_invalid_priority():
    bad = '{"item":{"id":1,"title":"Bad","priority":"urgent","due":null}}'
    try:
        parser.parse(bad)
    except exceptions.UnexpectedInput:
        pass
    else:
        raise AssertionError('Invalid priority should fail')

import json
from lark import Lark, exceptions
from util import gbnf_to_lark

with open('todo.gbnf') as f:
    GRAMMAR = f.read()

parser = Lark(gbnf_to_lark(GRAMMAR), start='start')

def test_good_example():
    good = '{"item":{"id":1,"title":"Buy milk","priority":"low","due":null}}'
    parser.parse(good)

def test_bad_example():
    bad = '{"item":{"id":"oops","title":"Buy","priority":"low","due":null}}'
    try:
        parser.parse(bad)
    except exceptions.UnexpectedInput:
        pass
    else:
        raise AssertionError('Invalid example parsed')

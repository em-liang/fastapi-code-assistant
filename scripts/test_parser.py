import tree_sitter_python as tspython
from tree_sitter import Language, Parser

PY_LANGUAGE = Language(tspython.language())
parser = Parser(PY_LANGUAGE)

code = b"""
def hello(name):
    return f"Hello, {name}"
"""

tree = parser.parse(code)
print(tree.root_node)
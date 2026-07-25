import os
import tree_sitter_python as tspython
from tree_sitter import Language, Parser

PY_LANGUAGE = Language(tspython.language())
parser = Parser(PY_LANGUAGE)

file_location = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(file_location, '..', 'ingest', 'files-used.txt'), "r") as f:
  content = f.read().split()
  for c in content: 
    with open(os.path.join(file_location, '..', 'ingest', c), 'r') as file:
        py = file.read()
        code = py.encode('utf-8')
        tree = parser.parse(code)
        print(tree.root_node)
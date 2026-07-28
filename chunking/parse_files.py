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
        #print(tree.root_node)

def return_type(tree):
  t = tree
  if hasattr(t, 'root_node'): t = tree.root_node
  if len(t.children) == 0: return
  else:
    for node in t.children:
        if node.type == 'class_definition' or node.type == 'function_definition' or node.type == 'decorated_definition':
          print(node.type)
        return_type(node)
  
with open(os.path.join(file_location, '..', 'ingest', './fastapi-repo/fastapi/applications.py'), 'r') as file:
  py = file.read()
  code = py.encode('utf-8')
  tree = parser.parse(code)
  print(tree.root_node.children[0].parent.type)
  return_type(tree)
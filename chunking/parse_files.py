import os
import tree_sitter_python as tspython
from tree_sitter import Language, Parser

PY_LANGUAGE = Language(tspython.language())
parser = Parser(PY_LANGUAGE)

file_location = os.path.dirname(os.path.abspath(__file__))

'''
with open(os.path.join(file_location, '..', 'ingest', 'files-used.txt'), "r") as f:
  content = f.read().split()
  for c in content: 
    with open(os.path.join(file_location, '..', 'ingest', c), 'r') as file:
        py = file.read()
        code = py.encode('utf-8')
        tree = parser.parse(code)
        print(tree.root_node)
'''

def return_class_name(tree, class_name):
  t = tree
  if hasattr(t, 'root_node'): t = tree.root_node
  if len(t.children) == 0: return
  else:
    for child in t.children:
      if child.type == 'class_definition':
        class_name = None
        print(child.type)
        print(class_name)
        class_name = child.children_by_field_name('name')[0].text
      if child.type == 'function_definition' or child.type == 'decorated_definition':
        print(child.type)
        print(class_name)
      return_class_name(child, class_name)
  
with open(os.path.join(file_location, '..', 'ingest', './fastapi-repo/fastapi/routing.py'), 'r') as file:
  py = file.read()
  code = py.encode('utf-8')
  tree = parser.parse(code)
  return_class_name(tree, class_name = None)
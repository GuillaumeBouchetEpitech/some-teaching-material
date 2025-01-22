import ast
# from ast2json import ast2json
import json

source_code = """
print("LOL")
"""

try:
  # tree = ast2json(ast.parse(source_code))
  tree = ast.parse(source_code)

  # print(json.dumps(tree, indent=4))
except SyntaxError as err:
  print(f'err: {err}')
  print(f'err.filename: "{err.filename}"')
  print(f'err.lineno: "{err.lineno}"')
  print(f'err.end_lineno: "{err.end_lineno}"')
  print(f'err.offset: "{err.offset}"')
  print(f'err.end_offset: "{err.end_offset}"')
  print(f'err.text: "{err.text}"')
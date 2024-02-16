from lark import Lark
from Evaluator import Evaluator
from grammar import grammar
import sys

# Crear el parser usando la gramática
parser = Lark(grammar, parser='lalr', transformer=Evaluator())

# Función para evaluar la expresión
def evaluate(expression):
  try:
    result = parser.parse(expression)
    return result
  except Exception as e:
    return f"Error: {e}"

# Ejemplos:
action = sys.argv[1]

if action == 'count':
  # Ejemplo: count -w prueba.txt
  expression = f"count {sys.argv[2]} {sys.argv[3]}"
elif action == 'translate':
  # Ejemplo: translate from=sp to=en file.txt fileTrad.txt
  expression = f"translate {sys.argv[2]} {sys.argv[3]} {sys.argv[4]} {sys.argv[5]}"
if action == 'speech':
  # Ejemplo: speech file.txt file.mp3
  expression = f"speech {sys.argv[2]} {sys.argv[3]}"

print(evaluate(expression))
from lark import Transformer, v_args

@v_args(inline=True)
class Evaluator(Transformer):

  def start(self, expr):
    return expr
  
  def expr(self, operations):
    return operations

  def operations(self, op):
    return op
  
  def count(self, flag, filename):
    with open(filename) as f:
      content = f.read()
      return len(content) if flag == '-c' else len(content.split(' '))

  def translate(self, lang_from, lang_to, f_from, f_to):
    from deep_translator import GoogleTranslator

    with open(f_from) as f:
      content = f.read()
      result = GoogleTranslator(source='auto', target=lang_to.lower()).translate(content)
      print(result)
      with open(f_to, 'w') as f:
        f.write(result)

  def speech(self, fileInt, fileOut):
    import pyttsx3

    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    with open(fileInt, 'r') as file:
      texto = file.read()

    engine.save_to_file(texto, fileOut)
    engine.runAndWait()

  def filename(self, fname):
    return fname
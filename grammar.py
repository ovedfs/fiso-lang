grammar = """

start: expr+

expr: operations
    
operations: count 
            | summary
            | translate 
            | speech

count: "count" FLAG filename

summary: "summary" filename filename

translate: "translate" "from=" FROM "to=" TO filename filename

speech: "speech" filename filename

FLAG: "-c" | "-w"
FROM: LETTER LETTER
TO: LETTER LETTER
filename: (LETTER 
            | ALPHANUMERIC 
            | EXTENSION)
      
LETTER: /[a-zA-Z]/
ALPHANUMERIC: /[a-zA-Z0-9.]+/
EXTENSION: /[a-zA-Z]+/

%import common.WS
%ignore WS
%ignore /\s+/
"""
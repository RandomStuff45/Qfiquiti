from lark import Lark

# Shared grammar for the language
grammar = """
    start: (statement | function_def)*

    statement: declaration
             | print_statement

    declaration: type IDENTIFIER "is" value
    print_statement: "print" "(" IDENTIFIER ")"

    function_def: "func" IDENTIFIER "(" args ")" "->" type "{" body "}"
    args: (IDENTIFIER ("," IDENTIFIER)*)?
    body: statement*

    type: "int" | "float" | "string" | "bool" | "dic"
    value: NUMBER    -> number
         | ESCAPED_STRING -> string
         | "true" | "false" -> bool

    %import common.CNAME -> IDENTIFIER
    %import common.NUMBER
    %import common.ESCAPED_STRING
    %import common.WS
    %ignore WS

        value: NUMBER                -> number
         | ESCAPED_STRING        -> string
         | "true" | "false"      -> bool
         | IDENTIFIER            -> variable
         | "(" value ")"

    expression: value
              | expression "+" value -> add
              | expression "-" value -> subtract
              | expression "*" value -> multiply
              | expression "/" value -> divide
              | expression "%" value -> mod
"""

parser = Lark(grammar, parser="lalr")

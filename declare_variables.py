from lark import Lark, Transformer, v_args

# Grammar definition for your language
grammar = """
    start: declaration

    declaration: type IDENTIFIER "is" value

    type: "int" | "float" | "string" | "bool" | "dic"
    value: NUMBER    -> number
         | ESCAPED_STRING -> string
         | "true" | "false" -> bool

    %import common.NUMBER
    %import common.ESCAPED_STRING
    %import common.WS
    %ignore WS
"""

# Create a parser
parser = Lark(grammar, parser='lalr')

# Transformer to handle parsing logic
class VariableProcessor(Transformer):
    def declaration(self, items):
        var_type, name, value = items
        print(f"Declared {var_type} variable '{name}' with value {value}")
        return (var_type, name, value)

    def number(self, items):
        return float(items[0]) if '.' in items[0] else int(items[0])
    
    def string(self, items):
        return str(items[0][1:-1])  # Strip quotes

# Example usage
code = "int x is 9"
tree = parser.parse(code)
processor = VariableProcessor()
processor.transform(tree)

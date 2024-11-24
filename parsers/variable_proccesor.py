class VariableProcessor:
    def __init__(self):
        self.variables = {}

    def handle_declaration(self, var_type, name, value):
        self.variables[name] = {"type": var_type, "value": value}
        print(f"Declared {var_type} variable '{name}' with value {value}")

    def get_variable(self, name):
        if name in self.variables:
            return self.variables[name]
        else:
            raise KeyError(f"Variable '{name}' not found.")

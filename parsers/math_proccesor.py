class MathProcessor:
    def __init__(self, variable_store):
        self.variable_store = variable_store  # Reference to VariableProcessor
    
    def evaluate(self, operation):
        """Recursively evaluate math operations."""
        if operation.data == "add":
            return self.evaluate(operation.children[0]) + self.evaluate(operation.children[1])
        elif operation.data == "subtract":
            return self.evaluate(operation.children[0]) - self.evaluate(operation.children[1])
        elif operation.data == "multiply":
            return self.evaluate(operation.children[0]) * self.evaluate(operation.children[1])
        elif operation.data == "divide":
            return self.evaluate(operation.children[0]) / self.evaluate(operation.children[1])
        elif operation.data == "mod":
            return self.evaluate(operation.children[0]) % self.evaluate(operation.children[1])
        elif operation.data == "variable":
            name = operation.children[0]
            return self.variable_store.get_variable(name)["value"]
        else:
            return float(operation.children[0]) if "." in operation.children[0] else int(operation.children[0])

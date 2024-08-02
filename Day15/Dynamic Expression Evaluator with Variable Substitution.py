def evaluate_expression(expression, variables):
    try:
        for var, value in variables.items():
            expression = expression.replace(var, str(value))
        
        result = eval(expression)
        
        return result
    
    except KeyError as e:
        return f"Error: Undefined variable {e.args[0]}"
    except Exception as e:
        return f"Error: {str(e)}"

expression = "a + b * (c - d)"
variables = {"a": 5, "b": 3, "c": 10, "d": 2}

print(evaluate_expression(expression, variables))
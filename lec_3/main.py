
def evaluate_expression(expression):
    try:
        for operator in ['+', '-', '*', '/']:
            if operator in expression:
                operand1, operand2 = expression.split(operator)
                operand1 = float(operand1)
                operand2 = float(operand2)

                if operator == '+':
                    result = operand1 + operand2
                elif operator == '-':
                    result = operand1 - operand2
                elif operator == '*':
                    result = operand1 * operand2
                elif operator == '/':
                    if operand2 == 0:
                        return "Error: Division by zero"
                    result = operand1 / operand2

                return f"Result: {result}"

        return "Error: Invalid operator"

    except ValueError:
        return "Error: Invalid input format"

print(evaluate_expression(input("Enter a mathematical expression (e.g., '2+3'): ")))

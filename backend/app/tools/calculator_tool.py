import ast
import operator


OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}


def _evaluate(node):
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value

        raise ValueError("Only numbers are allowed.")

    if isinstance(node, ast.UnaryOp):
        operator_function = OPERATORS.get(type(node.op))

        if operator_function is None:
            raise ValueError("Unsupported operator.")

        return operator_function(_evaluate(node.operand))

    if isinstance(node, ast.BinOp):
        operator_function = OPERATORS.get(type(node.op))

        if operator_function is None:
            raise ValueError("Unsupported operator.")

        left = _evaluate(node.left)
        right = _evaluate(node.right)

        return operator_function(left, right)

    raise ValueError("Invalid mathematical expression.")


def calculator(expression: str):
    """
    Safely calculate a mathematical expression.
    """

    expression = expression.strip()

    if not expression:
        raise ValueError("Expression cannot be empty.")

    tree = ast.parse(expression, mode="eval")

    return _evaluate(tree.body)
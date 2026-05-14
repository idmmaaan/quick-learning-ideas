import ast
import operator
import sys

class Calc(ast.NodeVisitor):

    _OP_MAP = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
    }

    _UNARY_MAP = {
        ast.USub: operator.neg,
        ast.UAdd: operator.pos,
    }

    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        op_type = type(node.op)

        if op_type not in Calc._OP_MAP:
            raise ValueError(f"Unsupported operator: {op_type}")

        return Calc._OP_MAP[op_type](left, right)

    def visit_UnaryOp(self, node):
        operand = self.visit(node.operand)
        op_type = type(node.op)

        if op_type not in Calc.Calc_UNARY_MAP:
            raise ValueError(f"Unsupported unary operator: {op_type}")

        return Calc._UNARY_MAP[op_type](operand)

    def visit_Constant(self, node):
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError("Only numbers are allowed")

    def visit_Expr(self, node):
        return self.visit(node.value)

    def visit_Module(self, node):
        return self.visit(node.body[0])

    def generic_visit(self, node):
        raise ValueError(f"Unsupported syntax")

    @classmethod
    def evaluate(cls, expression):
        tree = ast.parse(expression, mode="exec")
        return cls().visit(tree)
    
if __name__ == "__main__":

   if len(sys.argv) < 2:
        print("Usage: calc <expression>")
   else:
       expr = sys.argv[1]
       try:
           print(Calc.evaluate(expr))
       except SyntaxError:
           print("Invalid expression (check parentheses and syntax)")
       except Exception as e:
           print(f"Error: {e}")
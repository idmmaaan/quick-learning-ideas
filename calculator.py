import sys
import math
from typing import Optional

class Calc():

    OP_MAP = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b
    }
        
    def eval(exp: str)-> str:
        
        exprassion = Calc.find_operands(exp)
        print(exprassion)
        operand_a = exprassion[0]
        operand_b = exprassion[1]
        operator = exprassion[2]
        print(exp)
        
        return Calc.OP_MAP[operator](operand_a, operand_b)
    
    def find_operands(exp: str)-> list[int | str]:
        exp = exp.replace(" ", "").strip()
        result = []

        for key, token in enumerate(exp):
             if token in Calc.OP_MAP and key > 0 and key < len(exp) - 1:
                left = exp[key - 1]
                op = token
                right = exp[key + 1]
                result.append(left)
                result.append(right)
                result.append(op)

        return result
    
    def check_operator(operator: str) -> str:
        if operator in Calc.OP_MAP:
            return operator
        else: raise ValueError(f"Unsupported unary operator: {operator}")

        
if __name__ == "__main__":
  
    print(sys.argv)
    print(Calc.eval(sys.argv[1]))
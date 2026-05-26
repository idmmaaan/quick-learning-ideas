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

    __PARENTHESES_MAPPING = {
        '{' : '}',
        '[' : ']',
        '(' : ')'
    }

    def isValidParentheses(self, s: str) -> bool:
        stack = []
        
        for char in s:
            if char in self.__PARENTHESES_MAPPING:
                stack.append(char)
                
            elif char in self.__PARENTHESES_MAPPING.values():
                if stack and self.__PARENTHESES_MAPPING[stack[-1]] == char:
                    stack.pop() 
                else:
                    return False
                
        return len(stack) == 0
        
    def eval(exp: str)-> str:
        
        if not Calc.isValidParentheses(Calc, exp):
            raise ValueError("Invalid parentheses in expression")

        result = 0
        exprassion = Calc.find_operands(exp)

        for item in exprassion:
            operand_a = item[0]
            operand_b = item[1]
            operator = item[2]
            result += Calc.OP_MAP[operator](int(operand_a), int(operand_b))
        
        return str(result)

    def find_operands(exp: str)-> list[int | str]:
        exp = exp.replace(" ", "").strip()
        result = []

        for key, token in enumerate(exp):
             if token in Calc.OP_MAP and key > 0 and key < len(exp) - 1:
                item = []
                left = 0
                right = 0

                if exp[key - 1].isdigit():
                    left = exp[key - 1]

                left = exp[key - 1]
                op = token

                if exp[key + 1].isdigit():
                    right = exp[key + 1]

                right = exp[key + 1]
                item.append(left)
                item.append(right)
                item.append(op)
                result.append(item)

        return result
    
    def check_operator(operator: str) -> str:
        if operator in Calc.OP_MAP:
            return operator
        else: raise ValueError(f"Unsupported unary operator: {operator}")


if __name__ == "__main__":
  
    print(Calc.eval("(3 + 4) + 5"))
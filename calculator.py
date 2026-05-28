import re

class Calc():
    
    OP_MAP = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b
    }

    PARENTHESES_MAPPING = {
        '(' : ')'
    }
    
    def is_valid_parentheses(self, s: str) -> bool:
        stack = []
        
        for char in s:
            if char in self.PARENTHESES_MAPPING:
                stack.append(char)
                
            elif char in self.PARENTHESES_MAPPING.values():
                if stack and self.PARENTHESES_MAPPING[stack[-1]] == char:
                    stack.pop() 
                else:
                    return False
                
        return len(stack) == 0
        
    def eval(self, exp: str)-> str:
        valid = self.validate_expression(exp)

        tokens = Calc.tokenizer(self,exp)
        
        stack = []

        for i in tokens:
            if i.isdigit():
                stack.append(float(i))
            else:
                operand_b = stack.pop()
                operand_a = stack.pop()
                stack.append(self.OP_MAP[i](operand_a, operand_b))

        
        return stack.pop()

    def tokenizer(self, exp: str)-> list[str]:
        exp = exp.replace(" ", "").strip()

        operators = []
        operands = []
        
        for token in exp:

            if token.isdigit():
                operands.append(token)
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    operands.append(operators.pop())
                if operators:
                    operators.pop()
            elif token in self.OP_MAP:
                while operators and operators[-1] != '(' and operators[-1] in self.OP_MAP:
                    if self.operator_priority(token) <= self.operator_priority(operators[-1]):
                        operands.append(operators.pop())
                    else:
                        break
                operators.append(token)
        
        while operators:
            operands.append(operators.pop()) 
        

        return operands

    def operator_priority(self, operator: str) -> int:
        if operator in ("*", "/"):
            return 2
        elif operator in ("+", "-"):
            return 1
        else: raise ValueError(f"Unsupported unary operator: {operator}")

    def validate_expression(self, exp: str):

        exp = exp.replace(" ", "")

        full_pattern = r'^(?:-?(?:\d*\.\d+|\d+)|[()+\-*/])+$'

        if re.fullmatch(full_pattern, exp) is None:
            raise ValueError("Invalid symbol in expression")

        if not self.is_valid_parentheses(exp):
            raise ValueError("Invalid parentheses in expression")

        if re.search(r'[+\-*/]{2,}', exp):
            raise ValueError("Invalid operator sequence")
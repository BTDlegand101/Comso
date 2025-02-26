import math
import operator

calculations = []
operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "^": operator.pow,
    "sqrt": math.sqrt,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "asin": math.asin,
    "acos": math.acos,
    "atan": math.atan,
}

def list_ops():
    print("")
    print("Operations:")
    for operation in operations:
        print(operation)
    print("")

def setup(equation):
    main_list = []
    temp_n = ""
    for item in equation:
        if item in "1234567890.":
            temp_n += item
        elif item in operations:
            main_list.append(float(temp_n))
            main_list.append(item)
            temp_n = ""
    main_list.append(float(temp_n))
    calculations.append(main_list)

def calculate():
    for calculation in calculations:
        result = calculation[0]
        for i in range(1, len(calculation), 2):
            operator = calculation[i]
            next_number = calculation[i + 1]
            result = operations[operator](result, next_number)
        print(result)
    calculations.clear()
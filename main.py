def sum(n1: int, n2: int):
    return n1 + n2

def mult(n1: int, n2: int):
    return n1 * n2

def rest(n1: int, n2: int):
    return n1 - n2

def div(n1: int, n2: int):
    if n2 == 0:
        raise ZeroDivisionError
    return n1 / n2

num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
operator = input("Operator (one of: 'sum' for sum, 'rest' for rest, 'mult' for multiply, 'div' for divide): ")

res = None

if operator == "sum":
    res = sum(num1, num2)
elif operator == "rest":
    res = rest(num1, num2)
elif operator == "mult":
    res = mult(num1, num2)
elif operator == "div":
    res = div(num1, num2)

print(res)
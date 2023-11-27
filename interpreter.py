mathExpression = input("Expression: ")
x, y, z = mathExpression.split(" ")
# converts strings into float
x = float(x)
z = float(z)
if y == "+":
    expressionEval = x + z
elif y == "-":
    expressionEval = x - z
elif y == "*":
    expressionEval = x * z
elif y == "/":
    expressionEval = x / z

print(expressionEval)
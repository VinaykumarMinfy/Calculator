print("Enter the Expression:")
exp = input()
i = 0
num = ''

# Parse the first number
while i < len(exp) and exp[i].isdigit():
    num += exp[i]
    i += 1

res = int(num)

# Process the rest of the expression
while i < len(exp):
    op = exp[i]
    i += 1  # move to the next character after operator

    num = ''
    while i < len(exp) and exp[i].isdigit():
        num += exp[i]
        i += 1

    if num == '':
        break  # break if no number is found after operator

    if op == "+":
        res += int(num)
    elif op == "-":
        res -= int(num)
    elif op == "*":
        res *= int(num)
    elif op == "/":
        res /= int(num)

print(res)

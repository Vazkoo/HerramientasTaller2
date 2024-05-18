def division(num1, num2):
    if num2 == 0:
        print("ERROR: Division by zero")
    else:
        result = num1 / num2
        print(f'{num1} / {num2} is equal to {result}')
        return result
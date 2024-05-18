def module(num1, num2):
    if num2 == 0:
        print("SYNTAX ERROR")
    
    result = num1 % num2
    print(f'{num1} % {num2} is equal to {result}')
    return result
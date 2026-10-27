def calculator():
    try:
        
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        
        operation = input("Enter an operation (+, -, *, /, %, **): ").strip()
        
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation in ('/', '%'):
            
            try:
                if operation == '/':
                    result = num1 / num2
                else:
                    result = num1 % num2
            except ZeroDivisionError:
                print("Error: Division or modulus by zero is not allowed.")
                return
        elif operation == '**':
            result = num1 ** num2
        else:
            print("Error: Invalid operation entered.")
            return
            
        
        print(f"The result of {num1} {operation} {num2} is: {result}")
        
    except ValueError:
        print("Error: Invalid input. Please enter numerical values.")


if __name__ == "__main__":
    calculator()

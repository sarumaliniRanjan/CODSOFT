
def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operation."


def main():
    print("Simple Calculator")
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
        return

    print("Choose an operation: add, subtract, multiply, divide")
    operation = input("Enter the operation: ").strip().lower()

    result = perform_operation(num1, num2, operation)
    print(f"The result of {operation}ing {num1} and {num2} is: {result}")

# Run the main function
if __name__ == "__main__":
    main()

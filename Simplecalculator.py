
while True:
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("\nError: Division by zero is not allowed(If both first number,second number are zero then result=0 ).\n")
                continue
            result = num1 / num2
        else:
            print("\nInvalid operator. Please try again.\n")
            continue

        print(f"The result of ( {num1} {operator} {num2} ) is: {result}")
        another_calculation = input("\nDo you want to perform another calculation? (y for yes/n for no): ")
        print()
        if another_calculation.lower() != 'y':
            print("\nThank you for using the calculator. Goodbye!")
            break
    except:
        print("\nInvalid input. Please enter numeric values for numbers.\n")
            
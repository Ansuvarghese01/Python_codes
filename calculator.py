print("Welcome to Simple Calculator")
while True:
    # Options
    print(
        "1.Addition\n" 
        "2.Subtraction\n" 
        "3.Multiplication\n" 
        "4.Division\n" 
        "Enter Q to Exit")

    operation = input()

    if operation == 'Q':
        break

    num_1 = float(input("Enter the First Number: "))
    num_2 = float(input("Enter the Second Number: "))
    operation = int(operation)
    print()

    if operation == 1:
        result = num_1 + num_2
        print(f"{num_1} + {num_2} = {result}\n")

    elif operation == 2:
        result = num_1 - num_2
        print(f"{num_1} - {num_2} = {result}\n")

    elif operation == 3:
        result = num_1 * num_2
        print(f"{num_1} X {num_2} = {result}\n")

    elif operation == 4:
        if num_2 == 0:
            print("ERROR DIVISION BY ZERO!!!\n")
            continue
        result = num_1 / num_2
        print(f"{num_1} / {num_2} = {result}\n")

    else:
        print("Enter a Valid Option!!!\n")


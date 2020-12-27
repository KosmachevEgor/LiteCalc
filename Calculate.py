while True:
    print("Menu:")
    print("Enter 'add' to add two numbers")
    print("Enter 'substract' to subtract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'divide' to devide two numbers")
    print("Enter 'quit' to end the program")
    In = input(": ")
    if In == "quit":
        break
    elif In=="add":
        n1=float(input("Enter a number: "))
        n2=float(input("Enter another number: "))
        r=str(n1+n2)
        print("Answer: " + r)
    elif In=="substract":
        n1=float(input("Enter a number: "))
        n2=float(input("Enter another number: "))
        r=str(n1-n2)
        print("Answer: " + r)
    elif In=="multiply":
        n1=float(input("Enter a number: "))
        n2=float(input("Enter another number: "))
        r=str(n1*n2)
        print("Answer: " + r)
    elif In=="divide":
        n1=float(input("Enter a number: "))
        n2=float(input("Enter another number: "))
        r=str(n1/n2)
        print("Answer: " + r)
    else:
        print('Input Error')


#Simple Calculator

operator = input("Please enter your operator: ")
n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
if operator == "+":
    print( n1+n2)
elif operator == "*":
    print( n1*n2)
elif opt == 3:
    print(n1, '/', n2, '=', n1/n2)
elif opt == 4:
    print(n1, '-', n2, '=', n1-n2)
else:
    print("Invalid input")
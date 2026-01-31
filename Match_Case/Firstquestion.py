a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
sum= a+b
match sum%2:
    case 0:
        print("The sum is even.")
    case 1:
        print("The sum is odd.")
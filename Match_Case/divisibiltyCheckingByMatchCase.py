a = int(input("Enter your number : "))
match a:
    case _ if a%3==0 and a%5==0 :
        print("Number is divisible by both 3 and 5")
    case _ if a%5==0 :
        print("Number is divisible by 5")
    case _ if a%3==0 :
        print("Number is divisible by 3")
    case _ :
        print("Number is not divisible by either 3 or 5")

    
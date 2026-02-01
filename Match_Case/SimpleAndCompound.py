p = int(input("Enter your principal amount = "))
r = float(input("Enter your rate of interest = "))
t = float(input("Enter time in years = "))
SI = (p*r*t)/100
print("Simple Interest = ", SI)
CI = p*(pow((1+r/100),t))-p
print("Compound Interest = ", CI)
difference = CI - SI
diff = int(round(difference,0))
print("Difference between CI and SI = ", diff)

match diff:
    case _ if diff > 0:
        match diff:
            case _ if diff%2==0 and diff%5==0:
                print("Difference is even and multiple of 5")
            case _ if diff%5==0:
                print("Difference is multiple of 5")
            case _ if diff%2==0:
                print("Difference is even")
            case _:
                print("no special condition met")
    case _ if diff < 0:
        match diff:
            case _ if diff%3==0 and diff%7==0:
                print("Difference is multiple of 3 and 7")
            case _ if diff%7==0:
                print("Difference is multiple of 7")
            case _ if diff%3==0:
                print("Difference is multiple of 3")
            case _:
                print("no special condition met")
    case _:
        print("No difference between CI and SI")
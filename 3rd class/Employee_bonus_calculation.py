service = int(input("Enter the amount of years you have worked: "))
Sal = int(input("Enter your salary: "))

if service >= 5 and Sal < 50000:  # Check this specific case first
    print("You get a 15% bonus: ", Sal + (Sal * 3) / 20)
elif service >= 5:  # Then check service >= 5 (for Sal >= 50000)
    print("You get a 10% bonus: ", Sal + (Sal / 10))
elif Sal > 50000:
    print("You get a 5% bonus: ", Sal + (Sal / 20))
else:
    print(f"Your salary: {Sal}")
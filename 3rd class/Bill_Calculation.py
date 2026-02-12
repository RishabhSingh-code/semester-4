bill = int(input("Enter the units used: "))
if bill <= 100:
    print("the bill:",bill*3)
elif bill >100 and bill < 200:
    print("the bill: ",(bill - 100)*5 + 100*3)
elif bill > 200:
    print("the bill:",(bill-100)*5+(bill - 200)*7 + 100*3)
else:
    print("Check the code again")
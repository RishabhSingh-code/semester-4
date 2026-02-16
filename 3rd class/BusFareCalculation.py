age =float(input("Enter your age:"))
fare = float(input("Enter your fare:"))
if age >60:
    print("You will get 30% off: ",fare -fare*0.3)
elif 13<= age >=60:
    print("Full price: ",fare)
elif 5<age>=12:
    print("Half price: ",fare -fare*0.5)
else:
    print("Free for you")
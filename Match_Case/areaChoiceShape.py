choice = int(input("1. area of circle.\n 2.area of square.\n 3. area of rectangle.\n Enter your choice = "))
match choice:
    case 1:
        radius = float(input("Enter your radius : "))
        area = 3.14*radius*radius
        print("Area of circle is :",area)
    case 2:
        length = float(input("Enter your length : "))
        area = length * length
        print("Area of square : ",area)
    case 3:
        length = float(input("Enter your length : "))
        breadth = float(input("Enter your breadth : "))
        area = length*breadth
        print("Area of rectangle : ",area)
    case _ :
        print("Invalid Input")

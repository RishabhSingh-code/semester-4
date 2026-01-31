choice = int(input("1. volume of cube \n 2.volume of cuboid \n 3. Volume of cylinder \n Enter your choice = "))
match choice:
    case 1:
        length = float(input("Length of cube : "))
        area = length * length * length
        print("Volume of cube :",area)
    case 2:
        length = float(input("Enter your length : "))
        breadth = float(input("Enter your breadth : "))
        height = float(input("Enter your height : "))
        volume = length*breadth*height
        print("volume of cuboid : ",volume)
    case 3:
        radius = float(input("Enter your radius : "))
        height = float(input("Enter your height : "))
        area = 3.14*radius*radius*height
        print("volume of cylinder : ",area)
    case _ :
        print("Invalid Input")
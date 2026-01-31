age = int(input("Enter your age : "))
match age:
    case age if age < 18:
        print("You are a minor.")
    case age if 18 <= age < 60:
        print("You are an adult.")
    case _ if age >= 60:
        print("You are a senior citizen.")

word = input("Enter your Character :").strip().upper()
a = "AEIOU"
if word in a:
    print("Its a Vowel")
else:
    print("Its a Consonant")
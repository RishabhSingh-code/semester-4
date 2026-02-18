word =input("Enter your word: ").strip().upper()
vowels =('AEIOU')
count = 0
for char in word:
    if char in vowels:
        count +=1
print(count)
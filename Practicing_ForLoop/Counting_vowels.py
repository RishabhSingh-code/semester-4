x = input("enter anything : ").lower()
v = 'aeiou'
count = 0
for i in x :
    if i in v :
        count += 1
print(count )   
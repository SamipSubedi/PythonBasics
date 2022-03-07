i = 1
while i <=10:
    print(i)
    i = i+1
print("Next number is 11")

#For Loops

for letter in "Liverpool Football Club":
    print(letter)

friends = ["karim", "Beghan", "Sultan", "Raja"]
print(len(friends))
for friend in friends:
    print(friend)

for index in range(4, 11):
    print(index)

for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0:
        print("First iteration")
    else:
        print("Not First")

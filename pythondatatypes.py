#Working with Lists

friends = ["Kevin", "Ramin", "Darin", "Oscar", "Doby"]

print(friends[1])
print(friends[1:])
friends[2] = "Soup"
print(friends[1:4])

#List Functions

lucky_numbers = [4, 6 ,7 ,8, 9]
friends = ["Kevin", "Ramin", "Ramin", "Darin", "Oscar", "Doby"]

#friends.extend(lucky_numbers)

friends.append("Raju")
friends.insert(2, "Golmal")
friends.remove("Darin")

friends.pop()
#friends.clear()

print(friends)
print(friends.index("Doby"))
print(friends.count("Ramin"))
friends.sort()
print(friends)
friends2 = friends.copy()
print(friends2)


#Tuples


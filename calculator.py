num1 = input ("Enter a number: ")
num2 = input ("Enter another number: ")
result = float(num1) + float(num2)

#print(result)

#Mad Libs GAME
color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity name: ")


print("Roses are " +color)
print(plural_noun +" are blue")
print("I love "+ celebrity)

#Better Claculator

num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter  second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print((num1 * num2))
else:
    print("Invalid operator")
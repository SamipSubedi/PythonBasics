#user = input("Enter Your Name: ")
def sayhi(user, age):
    print("Hello " + user+ " Your age is " + age)
#sayhi(input("Enter your name "), input("Enter your age "))

#return statement

def cube(num):
   return num*num*num

result = cube(4)
#print(result)

#If Statements

is_male = False
is_tall = False

if is_male and is_tall:
    print("You are a male and tall")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not  male but tall")
else:
    print("You are not male and not tall")

#if statements comparisons

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(300,44,5))




character_name = "Ram"
item_num = 6
is_male = False
print("once " + character_name +"")
print("eat " + str(item_num) + "")
item_num = "8"
print("chicken still "+ character_name +"")
print("was not full with "+ item_num +" chicken")

# working with strings
phrase = "Hello World"
dam = " Its me"
print(phrase.lower())
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[4])
print(phrase.index("orld"))
print(phrase.replace("Hello", "Bye"))

#Working with numbers
print(4 * (6 + 3))
print(10 % 3)
my_num = 5
print(str(my_num) + " my number")
my_num = -5
print(abs(my_num))
print(pow(3, 2)) # 3 power 2
print(max(10, 68))
print(min(3, 2.9))
print(round(5.6765756))

from math import *

my_num = 9
print(floor(6.7)) # gives 6
print(ceil(6.2)) #gives 7
print(sqrt(4096))

#Getting Input from User

name = input("Enter a name: ")
day = input("Enter time of day: ")
print("My name is " + name + "")
print ("Hello " +name+ " Good" +day+ "")

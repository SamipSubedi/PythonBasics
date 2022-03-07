#Translating vowels

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "S"
            else:
                translation = translation + "s"
        else:
            translation = translation + letter

    return translation

print(translate(input("Enter a phrase: ")))

''''
Try Expect
'''
try:
    value = 10 / 0
    number = int(input("Enter a number : "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print("Invalid Input")
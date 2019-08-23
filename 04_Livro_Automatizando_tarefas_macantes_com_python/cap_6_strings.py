# Some methods with strings:
# spam = "Hello world!"
# spam = spam.upper()
# print(spam)
# spam = spam.lower()
# print(spam)

# print("How are you?")
# feeling = input()
# if feeling.lower() == "great":
#     print("I am great too")
# else:
#     print("Answer: " + feeling + " - I hope the rest of your day is good")

# spam = "Hello world!"
# print(spam.islower())
# print(spam.isupper())
# print("HELLO".isupper())
# print("HEllo".isupper())
# print("Hello".islower())
# print("hello".islower())
# print("123.hello".islower())  # It can mixe numbers

# print("heLlo".upper().lower())  # Always the last

# "test".isalpha()  # Return True if string has only letters and without empty values.
# "test".isalnum()  # Return True if string has letters and numbers but without empty values.
# "test".isdecimal()   # Return True if string has only decimal numbers and without empty values.
# "test".isspace()   # Return True if string has only spaces.

# it start ou end with the text
# "Hello World".startswith("Hello")  # or
# "Hello World".endswith("Hello")

# join() and split()
print(", ".join(["My", "name", "is", "python!"]))
print(" ".join(["My", "name", "is", "python!"]))
print("-".join(["My", "name", "is", "python!"]))
print("My", "name", "is", "python!".split())



# while True:
#     print("Say me your age: ")
#     age = input()
#     if age.isdecimal():  # Validation input
#         break
#     print("Please enter a number\n for your age")
#
# while True:
#     print("Say me your password: ")
#     password = input()
#     if password.isalnum():  # Validation input
#         break
#     print("Password can only have letters and numbers")

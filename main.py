import random
import json

# variables
my_num = 2

my_random_random = random.randint(1, 10) # generate a random number between 1 and 10.

my_string = "Hello World!"

my_string_1 = my_string.split() # ["Hello", "World!"]

my_string_1.pop()

my_array = ["Hey", "There"]

my_array.append("Friend")

my_int = 8

if my_int >= 10:
    print("Greater than or equal to 10")
elif my_int == 10:
    print("Equal to 10")
else:
    print("Not greater than or equal to 10")


def my_function():
    print("Hello World")
    x = [1,2,3]
    for i in range(len(x)):
        print(i)

my_function()


my_dictionary = dict({
    "data":"some data",
    1: "my number",
    myData: str("a string"),
    "":""
}) # dictionary is similar to a JavaScript object or a json file.


# print statements

# print(my_num, my_random_random)
# print(my_string)
# print(my_string_1)
# print(my_array)
# print(my_num,my_random_random,"\n",my_string,"\n",my_string_1,"\n",my_array)

# print(f"{my_num}, {my_random_random}, {my_string}, {my_string_1}, {my_array}")


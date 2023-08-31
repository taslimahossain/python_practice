print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:
def get_divisors(num):
    new_list = []
    for divisors in range(1, num + 1):
        if num % divisors == 0:
            new_list.append(divisors)
    print(new_list)
get_divisors(87)


print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:
def is_factor(num1, num2):
    # list.listnum1 = get_divisors(num1)
    # list.listnum2 = get_divisors(num2)
    if num1 == get_divisors(num2):
        print(True)
    elif num2 == get_divisors(num1):
        print(True)
    else:
        print(False)
is_factor(6, 78)
#

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:

def find_position(str):
    position = 0
    for i in range(0, len(alphabet)):
        if alphabet[i] == str:
            position = i
    print(position)

find_position("o")



print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:
def id_generator(name):
    # name= str(input("Enter name here: "))
    # id = ""
    for x in name:
        find_position(x)
    #     id += print(find_position(x))
    # print(id)
id_generator("bob")


print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:
# def password_generator(name):
#     password = 0
#     id_generator(name)
#     for i in ID:
#         password = password + i - 7
#
# password_generator("bob")
# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            print("False")
            break
    else:
        print("True")
is_prime(999)

print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:
def no_error(value):
    is_prime(value)


# -------------------------------------------------------------------------------------- #







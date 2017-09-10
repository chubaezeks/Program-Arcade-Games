#Exception Handling

# Divide by zero
try:
    x = 5/0
except:
    print("Error dividing by zero")

# Handling number conversion errors
try:
    x = int("fred")
except:
    print("Error converting fred to a number")

# Better handling of number conversion errors
number_entered = False
while not number_entered:
    number_string = input("Enter an integer: ")
    try:
        n = int(number_string)
        number_entered = True
    except:
        print("Error, invalid integer")

# Checking for an error when opening a file
# Error opening file
try:
    my_file = open("myfile.txt")
except:
    print("Error opening file")

# Handling different types of errors
import sys

# multiple errors
try:
    my_file = open("myfile.txt")
    my_line = myfile.readline()
    my_int = int(s.strip())
    my_calculated_value = 101 / my_int
except IOError:
    print("I/O error")
except ValueError:
    print ("Could not convert data into an interger.")
except ZeroDivisionError:
    print("Division by zero error")
except:
    print("Unexpected error:", sys.exc_info()[0])



# Exception Objects
# When you're linking to more information about the error, use the 'as' keyword
try:
    x = 5 / 0
except ZeroDivisionError as e:
    print(e)


# Exception may be generated with the raise command
def get_input():
    user_input = input("Enter Something: ")
    if len(user_input) == 0:
        raise IOError("Users entered nothing")

get_input()


# Write down the process in words
# We're writing code that asks a user for input,
# if it happens that the user entered nothing
# Rather than run an error, it notifies us through the raise command

# Now write it in code:
    # Create variable
def get_input():
    user_input = input("Enter your password: ")
    if len(user_input) == 0:
        raise IOError("You didn't enter a password. Please try again.")

get_input

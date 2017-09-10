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

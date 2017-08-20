# Import the my_functions.py file
import my_functions

# Foo call
my_functions.foo()


# rather than add a namespace everytime, we can simply import the library into
# the local namespace
from my_functions import *

#this no longer needs the namespace everytime, so...
foo()

# Creating a new excel sheet in python
from openpyxl import Workbook
import random

# Create an excel book
wb = Workbook()

# Grab the active worksheet
ws = wb.active

# Data can be assigned directly to cells
ws['A1'] = "This is a test"

# Rows can be appended
for i in range(200):
    ws.append([random.randrange(1000)])

# Save the file
wb.save("sample.xlsx")

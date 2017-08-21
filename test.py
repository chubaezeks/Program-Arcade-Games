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


# Install Beautiful Soup Library
"""
Example showing how to read from a web page
"""

from bs4 import BeautifulSoup
import urllib.request

# Read in the file
url = "http://www.espnfc.com/spi/rankings/_/view/fifa/teamId/203/mexico?cc=5901"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read(), "html.parser")

# Find the table with the Data
rank = soup.find("table").tbody

# Get a list of rows in the table
rows = rank.findAll("tr")

# Loop through each row
for row in rows:

    # Get a list of cells in the row
    cell = row.findAll("td")

    # Loop through each cell
    for cell in cells:
        print(cell.text, end=", ")

    # Ok, done with that row. Print a blank line so we go to the next.
    print()


    # Installing and working with Matplotlib library
    """
    Line chart with four values.
    The x-axis defaults to start at zero.
    """

    import matplotlib.pyplot as plt

    y = [1,3, 8, 4]

    plt.plot(y)
    plt.ylabel('Element Value')
    plt.xlabel('Element Number')

    plt.show()


    # Example 2
    """
    Line chart with four values.
    The x-axis values are specified as well.
    """
    import matplotlib.pyplot as plt

    x = [1, 2, 3, 4]
    y = [1, 3, 8, 4]

    plt.plot(x,y)

    plt.ylabel('Element Value')
    plt.xlael('Element')

    plt.show()

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
    plt.xlabel('Element')

    plt.show()

    # Example 3
    # Wondering what happens when the x-axis changes
    """
    This example shows two different series on the same graph.
    """
    import matplotlib.pyplot as plt

    x = [1, 2, 3, 4]
    y1 = [1,3, 8, 4]
    y2 = [2, 2, 3, 3]

    plt.plot(x, y1)
    plt.plot(x, y2)

    plt.ylabel('Element Value')
    plt.xlabel('Element')

    plt.show()


    # Example 4

    x = [1 2, 3, 4]
    y1 = [1, 3, 8, 4]
    y2 = [2, 2, 3, 3]

    plt.plot(x, y1, label = "Series 1")
    plt.plot(x, y2, label = "Series 2")

    legend = plt.legend(loc = 'upper center', shadow = True, fontsize = 'x-large')
    legend.get)frame(. set_facecolor('#00FFCC')

    plt.ylabel('Element Value')
    plt.xlabel('Element')

    plt.show()


    #Example 5
    """
    Annotating a graph
    """
    import matplotlib.pyplot as plt

    x = [1, 2, 3, 4]
    y = [1, 3, 8, 4]

    plt.annotate('Here',
                 xy = (2,3),
                 xycoords = 'data',
                 xytext = (-40, 20),
                 textcoords = 'offset points',
                 arrowprops = dict(arrowstyle=" ->",
                                    connectionstyle="arc, angleA=0,armA=30,rad=10"),
                 )

    plt.plot(x,y)

    plt.ylabel('Element Value')
    plt.xlabel('Element')

    plt.show()

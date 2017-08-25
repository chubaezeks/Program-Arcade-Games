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


    # Example 6
    """
    This shows how to set line styles and markers.
    """
    import matplotlib.pyplot as plt

    x = [1, 2, 3, 4]
    y1 = [1, 3, 8, 4]
    y2 = [2, 2, 3, 3]

    # First character: Line style
    # One of '-', '--', '-.', ':', 'None', ' ', "

    # Second character: color
    # http://matplotlib.org/1.4.2/api/colors_api.html

    # Third character: marker shape
    # http://matplotlib.org/1.4.2/api/markers_api.html

    plt.plot(x, y1, '-ro')
    plt.plot(x, y2, '--g^')

    plt.ylabel('Element Value')
    plt.xlabel('Element')


    plt.show()


    # Example 7
    """
    How to do a bar chart
    """

    import matplotlib.pyplot as plt

    x = [1,2,3,4]
    y = [1,3,8,4]

    plt.bar(x,y)

    plt.ylabel('Element Value')
    plt.xlabel('Element')

    plt.show()


    # Example 8
    """
    How to add x-axis value label
    """

    import matplotlib.pyplot as plt

    x = [1,2,3,4]
    y = [1,3,8,4]

    plt.plot(x,y)

        # You add the labels first as a list
        # To assign it to the x-axis, you call the xticks property and assign labels to it as an attribute
    labels = ['Frogs', 'Hogs', 'Bogs', 'Slogs']
    plt.xticks(x,labels)

    plt.ylabel('ELement Value')
    plt.xlabel('Element')

    plt.show()


    # Example 9
    """
    Using the numpy package to graph a function over a range of numbers
    """

    import numpy
    import matplotlib.pyplot as plt

        # to get the values of x, get the arange function and pass the following numbers through it
        # to get the y values, pass whatever you're trying to get through the sin function.
        #You can also call other attributes of numpy within the function

    x = numpy.arange(0.0, 2.0, 0.011)
    y = numpy.sin(2 * numpy.pi * x)

    plt.ylabel('Element Value')
    plt.xlabel('Element')

    plt.show()


    # Example 10
    """
    Use 'fill' to fill in the graph
    """

    import numpy
    import matplotlib.pyplot as plt

    x = numpy.arange(0.0, 2.0, 0.011)
    y = numpy.sin(2 * numpy.pi * x)

    # Blue stands for blue. 'Alpha' stands for the transparency
    plt.fill(x,y, b, alpha = 0.5)

    plt.ylabel('Element Value')
    plt.xlabel('Element')

    plt.show()


    # Example 11
    """
    Create a pie chart.
    """

    # Labels for the pie chart
    labels = ["Ameerah", "Shari", "Zainab", "Oge", "Priya"]

    # Sizes for each label
    sizes = [12, 21, 11, 9, 34]

    # colors
    # Get the colors from this list
    colors = ['blue', 'red', 'green', 'purple', 'brown']

    # How far out to pull a slice
    explode = (0, 0, 0, 0.01, 0)

    # Set aspect ratio to be equal so the pie is drawn as a circle
    plt.axis('equal')


    # Finally plot the chart
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1%%', shadows = True, startangle=90)

    plt.show()


    #Example 12
    """
    Create a candlestick chart for a stock
    """

    import matplotlib.pyplot as plt
    from matplotlib.dates import DateFormatter, WeekdayLocator,\
         DayLocator, MONDAY
    from matplotlib.finance import quotes quotes_historical_yahoo_ohlc, candlestick_ohlc

    # Grab the stock data between these dates
    date1 = (2014, 10, 13)
    date2 = (2014, 11, 13)

    # Go to the web and pull the stock info
    quotes = quotes_historical_ohlc('AAPL', date1, date2)
    if len(quotes) == 0:
        raise SystemExit

    # Set up the graph
    fig, ax = plt.subplots()
    fig.subplots_adjust(bottom=0.2)

    # Major ticks on Mondays
    mondays = WeekdayLocator(MONDAY)
    ax.xaxis.set_major_locator(mondays)

    # Minor ticks on all days
    alldays = DayLocator()
    ax.aaxis.set_minor_locator(alldays)

    # Format the days
    weekFormatter = DateFormatter('%b %d') # e.g., Jan 12
    ax.xaxis.set_major_formatter(weekFormatter)
    ax.xaxis_date()

    candlestick_ohlc(ax, quotes, width=0.6)

    ax.autoscale_view()
    plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')

    plt.show()

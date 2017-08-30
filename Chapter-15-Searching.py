# Reading from a File

file = open("super_villians.txt")

for line in file:
    line = line.strip()
    print(line)

file.close()


# Reading into an array
# Read in a file from disk and put it in an array.
file = open("super_villians.txt")

name_list = []
for line in file:
    line = line.strip()
    name_list.append(line)

file.close()

# To verify that the file was read into the array
print ( "There were", len(name_list)), "names in the file."

# An alternative
for name in name_list:
    print(name)


#Linear Search
key = "Morgiana the Shrew"

i = 0
while i < len(name_list) and name_list[i] != key:
    i += 1

if i < len(name_list):
    print( "The name is at posiiton", i)
else:
    print( "The name was not in the list.")



# Variations on the linear Search
Alien class
class Alien:
    """Class that defines an alien"""
    def __init__(self, color, weight):
        """ Constructor. Set name and color"""
        self.color = color
        self.weight = weight


# To create a function to chec if it has the property we're looking.
# In this case,the

def has_property(my_alien):
    """ Check to see if an item has a property.
    In this case, is the alien green? """
    if my_alien.color.upper() = "GREEN":
        return True
    else:
        return False     

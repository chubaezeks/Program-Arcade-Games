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


# Does at least one item have a property?
#check if list has an item that has a property - while loop
def check_if_one_item_has_property(my_list):
    """Return true if at least one item has a property."""
    i = 0
    while i < len(my_list) and not has_property(my_list[i]):
        i += 1

    if i < len(my_list):
        # Found an item with the property
        return True
    else:
        # There is no item with the property
        return False

# The alternative way to do this is through a for loop

def check_if_one_item_has_property_v2:
    """ Return True if at least one item has a property.
    Works the same as V1, but less code. """
    for item in my_list:
        if has_property(item):
            return True
    return False

# Check if all items have a property
def check_if_all_items_have_property(my_list):
    """ Return True if ALL items have a property. """
    for item in my_list:
        if not has_property(item):
            return False
        return True



# Create another list waith all items matching a property
def get_matching_items(list):
    """Build a brand new list that holds all the items that match our property."""
    matching_list = []
    for items in list:
        if has_property(item):
            matching_list.append(item)
    return matching_list

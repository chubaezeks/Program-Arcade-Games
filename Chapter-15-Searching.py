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


#Practicing Classes and trying to really understand the differences between attributes, class, and instance of a class.
class Vehicle():



car = Vehicle()
car.type = tesla
car.price = $50000
car.tech = electronic

#name of the class
class Girls():

    #Attributes of the class being defined
    age = 28
    height = 5.9
    school = Yale

# This creates an instance of the class i.e. a character i.e. an object. An object is the instance of a class
# Here we equate this instance to a variable "exes".
my_ex = Girls()

my_ex.name = "Oge"
my_ex.age = 25
my_ex.height = 5.9

my_ex_lover = Girls()
my_ex_lover.name = "Modupe"
my_ex_lover.age = 28
my_ex_lover.height = 5.4

def NoLongerFriends(my_exes):
    print (my_exes.name, my_exes.age, my_exes.height)

display_character(my_ex)
display_character(my_ex_lover)

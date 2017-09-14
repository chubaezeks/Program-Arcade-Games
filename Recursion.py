# Controlling recursion levels

def f(level):
    # print the level we are at
    print ("Recursion call, level", level)
    # If we haven't reached level ten...
    if level < 10:
    # Call this function again
    # And add another one to the level
    f(level + 1)

# Start the recursive calls at level 1
f(1)



#Non-Recursive Factorial

# This program calculates a factorial
# WITHOUTH using recursion
def factorial_nonrecursive(n):
    answer = 1
    for i in range(2, n +1):
        answer = answer * i
    return answer

#Recursive factorial

# This porgram calculates a factorial with recursion
def factorial_recursive(n):
    if n == 1:
        return 1
    elif n > 1:
        return n * factorial_recursive(n - 1)

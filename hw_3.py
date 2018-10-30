# Name: Jaymo Kim
# hw3.py
import math
import random
##### Template for Homework 3, exercises 1 -  ######


# ********** Exercise 1 **********

# Define is_divisible function here
##### YOUR CODE HERE #####
def is_divisible(m, n):
    if(n == 0):
        return("Error! You cannot divide by 0!")
    else:
        return(m % n == 0)

# Test cases for is_divisible
## Provided for you... uncomment when you're done defining your function

print(is_divisible(10, 5))  # This should return True
print(is_divisible(18, 7))  # This should return False
print(is_divisible(42, 0))  # What should this return? It gives an error!

# ********** Exercise 2 **********

# Define not_equal function here
##### YOUR CODE HERE #####
def not_equal(a, b):
    if(a == b):
        return(False)
    else:
        return(True)

# Test cases for not_equal
##### YOUR CODE HERE #####
print(not_equal("hi", "hello"))  # This would return True
print(not_equal(1004, 1004))  # This would return False
print(not_equal(True, False))  # This would return True

# ********** Exercise 3 **********

## 1 - multadd function
##### YOUR CODE HERE #####
def multadd(a ,b, c):
    return(a * b + c)

## 2 - Equations
##### YOUR CODE HERE #####
print(multadd(1, 2, 3))  # This should return 1 * 2 + 3 = 5
print(multadd(10, 10, 10))  # This should return 10 * 10 + 10 = 110
print(multadd(0.5, 4, 0.7))  # This should return 0.5 * 4 + 0.7 = 2.7

# Test Cases
angle_test = multadd(0.5, math.cos(multadd(math.pi, 0.25, 0)), math.sin(multadd(math.pi, 0.25, 0)))
print("sin(pi/4) + cos(pi/4)/2 is:")
print(angle_test)

ceiling_test = multadd(2, math.log(12, 7), math.ceil(multadd(276, 1/19, 0)))
print("ceiling(276/19) + 2 log_7(12) is:")
print(ceiling_test)


# ********** Exercise 4 **********

## 1 - rand_divis_3 function
##### YOUR CODE HERE #####
def rand_divis_3():
    ran = random.randint(0, 100)
    return(ran % 3 == 0)

# Test Cases
##### YOUR CODE HERE #####
print(rand_divis_3())
print(rand_divis_3())
print(rand_divis_3())
print(rand_divis_3())
print(rand_divis_3())
# I hope one of these tests returns True...

#
#  I am learning Python functions
# Pratyakcha Upadhyay
#


# TODO: define a basic function
def func1(): 
    print("I am a function")

# TODO: function that takes arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)



# TODO: function that returns a value
def cube(x):
    return x * x * x

# TODO: function with default value for an argument
def func3(num, y=1):
    result = 1
    for i in range(y):
        result = result  * num
    return result
    
# TODO: function with variable number of arguments
def func4(*args):
   result = 0
   for x in args:
       result = result + x 
   return result



# func1()
# print(func1())
# print(func1)



# func2 (10,20)
# print(func2(10,20))
# print(cube(5))

# print(func3(3))
# print(func3(3, 4))
# print(func3(y = 2, num = 3))


print(func4(3,7,3,1))

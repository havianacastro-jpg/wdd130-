import math
 # import the libraly we will use import math
 
# area of a square
side = float (input("what is the length of a side of the square?"))
area= side ** 2
print (f"the area of the square is : {area}")

# area of a rectangule 
length = float (input("what is the length of rectangule"))
width = float (input("what is the width of the rectangule"))
area = length * width
print (f"the area of the rectangule is :{area}")

# area of the circle
radius= float (input("what is the radius of the circle"))
# we could usa 3.14 as shown on the next line
# area = 3.14 * (radius ** 2)
# or we can use the math libraly, which will be more precise
area = math.pi * (radius ** 2)
print (f"the area of the circle is : {area}") 
#loop to print numbers from 0 to 10
print("numbers from 0 to 10:")
for i in range(11):
   #print(i)
#for loop to print numbers from 1 to 10
 print("numbers from 1 to 10:")
for i in range(10):
    print(i)

#for loop to print numbers from 1 to 10 with increament of +2
print("numbers from 1 to 10:")
for i in range(1,10,2):
    print(i)
#radius of a circle, using the input function
radius_input =input("Enter the radius of a circle:")
radius = float(radius_input)
print(f" The radius of the circle is: {radius}")
import math
pi_value = math.pi
print(f"The mathematical constant of pi is approximately: {pi_value}")
radius_input = input("Enter the radius of a circle")
radius = float(radius_input)
area = math.pi * radius ** 2
print(f"The area of the circle with radius {radius} is: {area}")
#Length of the rectangle using input funtion
length_input = input("Enter the length of the rectangle:")
length = float(length_input)
print(f"The length of the rectangle is:{length}")
#width of the rectangle using input funtion
width_input = input("Enter the width of the rectangle:")
width = float(width_input)
print(f"The width of the rectangle is:{length}")
#Area of the rectangle
area = length * width
print (f"The area of the rectangle is: {area}")
#import math
#given area values
area_circle = 314
area_rectangle = 150
length_rectangle = 15
if area_circle > 0:
    radius_circle = math.sqrt(area_circle / math.pi)
    print(f"The radius of the circle is: {radius_circle}")
else:
    print("The input parameters are not greater than o; you can't compute the area of the circle.")
if area_rectangle > 0 and length_rectangle > 0:
    width_rectangle = area_rectangle / length_rectangle
    print(f"The width of the rectangle is: {width_rectangle}")
else:
    print("The input parameters are not greater than 0; you can't compute the area of the rectangle.")



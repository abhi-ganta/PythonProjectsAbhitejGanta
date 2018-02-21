import math

paint_can = 400
door_area = 30
window_area= 20

length = input("Enter length")
height = input("Enter height")
width = input("Enter width")
numDoors = input("Enter the number of doors")
numWindows = input("Enter the number of windows")

totalArea = (2*length*height) + (2*height*width) + (2*length*width) - (numDoors*door_area) - (numWindows*window_area)

paintRequired = math.ceil(totalArea/paint_can)

print ('Length: ' + str(length))
print ('Height: ' + str(height))
print ('Width: ' + str(width))
print ('Number of Doors: ' + str(numDoors))
print ('Number of Windows: ' + str(numWindows))
print ('Paint Cans required is: ' +str(paintRequired))
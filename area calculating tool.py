print"AREA CALCULATING TOOL"
print"CHOICE   FIND"
print" 1.     Area of SQUARE"
print" 2.     Area of RECTANGLE"
print" 3.     Area of TRIANGLE"
print" 4.     Area of CIRCLE"

c = input ("Enter any Choice = ")
if(c==1):
 s = input("enter any side of the square = ")
 a = s*s
 print"Area = ",a
elif(c==2):
 l = input("enter length = ")
 b = input("enter breadth = ")
 a = l*b
 print"Area = ",a
elif(c==3):
 x = input("enter first side of triangle = ")
 y = input("enter second side of triangle = ")
 z = input("enter third side of triangle = ")
 s = (x+y+z)/2
 A = ((s-x)*(s-y)*(s-z))**0.5
 print"Area=",A
elif(c==4):
 r = input("enter radius = ")
 pi = 22/7
 a = (pi*r)^2
 print"Area = ",a
else:
 print"Wrong input"
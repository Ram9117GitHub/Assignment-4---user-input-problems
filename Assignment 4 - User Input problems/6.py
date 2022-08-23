'''Write a python script to calculate the area of Triangle. Number is entered by the user.'''
a = float(input("Enter first length of side :"))
b = float(input("enter second length of side :"))
c = float(input("Enter third length of side :"))
s = a+b+c/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("Area of Triangle is ",area)


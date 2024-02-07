import math

def radian():
    degrees=int(input("Input degree: "))
    radian=(degrees*math.pi)/180
    print("Output radian:",radian)

radian()

def  trapezoid():
    height=int(input("Height: "))
    a=int(input("First value: "))
    b=int(input("Second value: "))
    area=((a+b)*height)/2
    print("Area trapezoid:",area)

trapezoid()

def r_polygon():
    sides=int(input("Number of sides:"))
    length_sides=int(input("Length of a side: "))
    a=length_sides/(2*math.tan(math.pi/sides))
    area=a*sides*length_sides/2
    print("Area the palygon:",area)

r_polygon()


def parallelogram():
    length=float(input("Length: "))
    height=float(input("Height: "))
    area=length*height
    print(area)

parallelogram()
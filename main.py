import math

print("Ax^2 + Bx + C = 0")
a = int(input("A= "))
b = int(input("B= "))
c = int(input("C= "))

d = b * b - 4 * a * c

if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print(x1,x2)
if d==0:
    x = (-b ) / (2 * a)
    print(x)
if d<0:
    print("нет корней")


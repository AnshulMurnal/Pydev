import math
pi = 3.14
print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(abs(pi))
print(pow(pi,555))
print(math.sqrt(pi))
A = 22200
B = 233432
C = 4244.2
print(max(A,B,C))
print(min(A,B,C))
pi = 3.14
pi2 = 22/7
radius = float(input("\nEnter the radius: "))
def area():
    if radius % 7:
        return radius ** 2 * pi2
    else:
        return radius ** 2 * pi
result = area()
print("\nThe result is: "+str(result))

# Python program to find roots of quadratic equation
import math


# function for finding roots
def equationroots(a, b, c):
    # calculating discriminant using formula
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))

    # checking condition for discriminant
    if dis > 0:
        print((-b + sqrt_val) / (2 * a))
        print((-b - sqrt_val) / (2 * a))

    elif dis == 0:
        print(-b / (2 * a))

        # when discriminant is less than 0
    else:
        print(- b / (2 * a), " + i", sqrt_val)
        print(- b / (2 * a), " - i", sqrt_val)

    # Driver Program


a = float(input("\nEnter the value of a: "))
b = float(input("\nEnter the value of b: "))
c = float(input("\nEnter the value of c: "))

# If a is 0, then incorrect equation
if a == 0:
    print("\nInvalid quadratic equation")

else:
    equationroots(a, b, c)
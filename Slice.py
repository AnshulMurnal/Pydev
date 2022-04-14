website = str(input("\nenter a website link: "))
slice1 = slice(7, -4)
print("The website is " + website[slice1])

a = float(input("\nEnter the length of a side of triangle: "))
b = float(input("\nEnter the length of another side of triangle: "))


def hypotenuse():
    return (a ** 2 + b ** 2) ** 0.5
c = hypotenuse()


print("\nThe hypotenuse of the triangle is: " + str(c))

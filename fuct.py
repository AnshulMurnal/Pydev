for i in range(100,220):
    print(i)


name = input("\nEnter your name: ")
for i in name:
    print(i)

number = float(input("\nEnter a number: "))
number2 = float(input("\nEnter another number: "))
def compare(number,number2):
    if number > number2:
        print("The"+str(number)+" is greater than "+str(number2))
    elif number < number2:
        print("The" + str(number2) + " is greater than " + str(number))
    else:
        print("The numbers are equal")

result = compare(number,number2)
print(result)

# To convert binary number to decimal
number = input('Enter a Binary number:')
decimal_number = int(number, 2)
print('The decimal conversion is:', decimal_number)

# To convert decimals to binary number

def binary(decimal):
    if decimal > 0:
        binary(int(decimal / 2))
        print(decimal % 2, end='')


decimal = int(input("\nEnter a number : "))
binary(decimal)

'''
######### Check whether the last digit is even #######
number = int(input("Enter a number: "))

last_digit = number % 10

if last_digit % 2 == 0:
    print("Last digit is even")


########Check Whether Last Digit Is Odd########
number = int(input("Enter a number: "))

last_digit = number % 10

if last_digit % 2 != 0:
    print("Last digit is odd")



####### Check Whether Last Digit Is 5 #######
number = int(input("Enter a number: "))

last_digit = number % 10

if last_digit == 5:
    print("Last digit is 5")

##########  Check Whether Last Digit Is 0  ############
number = int(input("Enter a number: "))

last_digit = number % 10

if last_digit == 0:
    print("Last digit is 0")

########## Check Whether First Digit Is Greater Than 5 ########
number = int(input("Enter a number: "))

while number >= 10:
    number = number // 10

if number > 5:
    print("First digit is greater than 5")


######### Check Whether First Digit Is Even #######
number = int(input("Enter a number: "))

while number >= 10:
    number = number // 10

if number % 2 == 0:
    print("First digit is even")


########## Check Whether First and Last Digits Are Equal ########

number = int(input("Enter a number: "))

last_digit = number % 10

while number >= 10:
    number = number // 10

first_digit = number

if first_digit == last_digit:
    print("First and last digits are equal")


########## First Digit Greater Than Last Digit #########
number = int(input("Enter a number: "))

last_digit = number % 10

while number >= 10:
    number = number // 10

first_digit = number

if first_digit > last_digit:
    print("First digit is greater than last digit")


##########  First Digit Less Than Last Digit  #########
number = int(input("Enter a number: "))

last_digit = number % 10

while number >= 10:
    number = number // 10

first_digit = number

if first_digit < last_digit:
    print("First digit is less than last digit")

######### Check Whether Number Is 3-Digit #######
number = int(input("Enter a number: "))

if number >= 100 and number <= 999:
    print("3-digit number")

######### Check Whether Number Is 4-Digit ########
number = int(input("Enter a number: "))

if number >= 1000 and number <= 9999:
    print("4-digit number")

####### Check Whether Number Is Palindrome ######
number = int(input("Enter a number: "))

original = number
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

if original == reverse:
    print("Palindrome")

######### Sum of Digits Greater Than 10 #########
number = int(input("Enter a number: "))

temp = number
total = 0

while temp > 0:
    digit = temp % 10
    total = total + digit
    temp = temp // 10

if total > 10:
    print("Sum of digits is greater than 10")


######## Sum of Digits Is Even ########
number = int(input("Enter a number: "))

temp = number
total = 0

while temp > 0:
    digit = temp % 10
    total = total + digit
    temp = temp // 10

if total % 2 == 0:
    print("Sum of digits is even")
'''
######### First and Last Digits Have Same Parity#########

number = int(input("Enter a number: "))

last_digit = number % 10

while number >= 10:
    number = number // 10

first_digit = number

if first_digit % 2 == last_digit % 2:
    print("First and last digits have same parity")

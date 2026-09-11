
####### chech positive number #####
num = int(input("Enter number: "))

if num > 0:
    print("Positive")

####### check negative number ###
num = int(input("Enter number: "))

if num < 0:
    print("Negative")


##### check zero ####
num = int(input("Enter number: "))

if num == 0:
    print("Zero")

######## check even number ######

num=int(input("Enter number:"))
if num%2==0:
    print("Even number")

####### check odd number ###

num=int(input("Enter number:"))

if num%2!=0:
    print("odd number")



##### check number greater than 100 #####
num=int(input("Enter number:"))

if num>100:
    print("Greater than number")



##### check given numbers are equal ####

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a == b:
    print("Both numbers are equal")


#### Check First Number Is Greater   ####
a=int(input("enter number:"))
b=int(input("enter number:"))
if a>b:
    print("Greater")

age=int(input("enter age:"))
if age>18:
    print("Eligible")


#######   Check whether a number is divisible by 3  #########

num=int(input("enter a number:"))
if num%3==0:
    print("Divisible")


###########  Check whether a number is divisible by both 3 and 5######

num=int(input("Enter a number:"))
if num%3 == 0 and num % 5 == 0:
    print("Divisible")



######## Check Positive AND Even #####
num=int(input("Enter a number:"))
if num>0:
    print("positive")
if num%2==0:
    print("even")


###### Check Last Digit is Even ######
num=int(input("Enter a num:"))
digit=num%10
if digit%2==0:
    print("yes")


a=int(input("enter number:"))
b=int(input("enter number:"))
c=int(input("enter number:"))
if a>b and a>c:
    print("a is largest")
if b>c and b>a:
    print("b is larggest")
if c>a and c>b:
    print("c is largest")


a=int(input("enter number:"))
b=int(input("enter number:"))
c=int(input("enter number:"))
if a==b and b==c and a==c:
    print("equal")


#########  Smallest of 3 Numbers   ######

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a < b and a < c:
    print("a is smallest")

if b < a and b < c:
    print("b is smallest")

if c < a and c < b:
    print("c is smallest")


######## Check All Three Numbers Are Equal #####

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a == b and b == c:
    print("All numbers are equal")


######## Check All Three Numbers Are Different  ########

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a != b and b != c and a != c:
    print("All numbers are different")

####### Exactly Two Numbers Are Equal #####


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
    print("Exactly two numbers are equal")


##### First Digit of a 3-Digit Number ####
num = int(input("Enter number: "))
first = num // 100
if num >= 100 and num <= 999:
    print(first)

###### First Digit and Last Digit Are Equal ##


num = int(input("Enter 3-digit number: "))

if num >= 100 and num <= 999:
    first = num // 100
    last = num % 10

    if first == last:
        print("First and last digits are equal")


######## First Digit Greater Than Last Digit ########
num = int(input("Enter 3-digit number: "))

if num >= 100 and num <= 999:
    first = num // 100
    last = num % 10

    if first > last:
        print("First digit is greater than last digit")

####### Number Is Palindrome ########
num = int(input("Enter 3-digit number: "))

if num >= 100 and num <= 999:

    first = num // 100
    last = num % 10

    if first == last:
        print("Palindrome")

######## Placement Eligibility ######
cgpa = float(input("Enter CGPA: "))
backlogs = int(input("Enter backlogs: "))
attendance = float(input("Enter attendance: "))

if cgpa >= 7 and backlogs == 0 and attendance >= 75:
    print("Eligible for placement")


#### Discount eligibility ###
amount = float(input("Enter purchase amount: "))
member = int(input("Are you a member? 1-Yes 0-No: "))

if amount >= 5000 and member == 1:
    print("Eligible for discount")

######### Largest of 3 Without max() #######


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

largest = a

if b > largest:
    largest = b

if c > largest:
    largest = c

print("Largest =", largest)


######### Second Largest of 3 Numbers #######

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    if b > c:
        print("Second largest =", b)
    if c > b:
        print("Second largest =", c)

if b > a and b > c:
    if a > c:
        print("Second largest =", a)
    if c > a:
        print("Second largest =", c)

if c > a and c > b:
    if a > b:
        print("Second largest =", a)
    if b > a:
        print("Second largest =", b)

########   Three Numbers in Increasing Order #########

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a < b and b < c:
    print("Increasing order")


######## Check Number is a Perfect Square ########

num = int(input("Enter number: "))

root = int(num ** 0.5)

if root * root == num:
    print("Perfect square")


###### Check Number is a Perfect Cube ########
num = int(input("Enter number: "))

root = round(num ** (1 / 3))

if root * root * root == num:
    print("Perfect cube")

########## Check Number is Both Even and Perfect Square #####

num = int(input("Enter number: "))

root = int(num ** 0.5)

if num % 2 == 0 and root * root == num:
    print("Even perfect square")


######## Armstrong Number ######
num = int(input("Enter number: "))

original = num
sum = 0

if num >= 100 and num <= 999:

    digit = num % 10
    sum = sum + digit ** 3
    num = num // 10

    digit = num % 10
    sum = sum + digit ** 3
    num = num // 10

    digit = num % 10
    sum = sum + digit ** 3

    if sum == original:
        print("Armstrong number")



######## Perfect Number #########


num = int(input("Enter number: "))

sum = 0

if num > 0:

    for i in range(1, num):
        if num % i == 0:
            sum = sum + i

    if sum == num:
        print("Perfect number")









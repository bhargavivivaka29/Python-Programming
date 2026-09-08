###  Arthimetic operators ####
a = 20
b = 6

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)

### Assignment operators ###
x = 10

x += 5
print(x)

x -= 3
print(x)

x *= 2
print(x)

x //= 4
print(x)

x %= 3
print(x)

###  Comparision operators ###
a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


### Logical operators ###
age = 20
marks = 85

print(age >= 18 and marks >= 40)
print(age < 18 or marks >= 40)
print(not(age >= 18))


### Identity operators ###
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)
print(a is c)
print(a is not c)


### membership operators ### 
numbers = [10, 20, 30, 40]

print(20 in numbers)
print(50 in numbers)
print(50 not in numbers)


### Bitwise operators ###
a = 5
b = 3

print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)
print("NOT:", ~a)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)


##### Even or Odd ########
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


############ positive ,negative or zero ######

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


########## Largest of two numbers #########
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest:", a)
else:
    print("Largest:", b)



######### divisible by 5 and 10 #####
num = int(input("Enter a number: "))

if num % 5 == 0 and num % 10 == 0:
    print("Divisible by both 5 and 10")
else:
    print("Not divisible by both")



### swap two numbers ####
a = 10
b = 20

a, b = b, a

print("a =", a)
print("b =", b)

###### extract digits #####
num = 583

ones = num % 10
tens = (num // 10) % 10
hundreds = num // 100

print("Ones =", ones)
print("Tens =", tens)
print("Hundreds =", hundreds)


##### sum of digits ####
num = 583

ones = num % 10
tens = (num // 10) % 10
hundreds = num // 100

total = ones + tens + hundreds

print(total)

###### reverse of a digit #####
num = 583

ones = num % 10
tens = (num // 10) % 10
hundreds = num // 100

reverse = ones * 100 + tens * 10 + hundreds

print(reverse)

###### first and last ######
num = 583

first = num // 100
last = num % 10

print("First =", first)
print("Last =", last)


#### largest of three numbers ########
a = 10
b = 25
c = 15

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)

######## smallest of three numbers #####
a = 10
b = 25
c = 5

if a <= b and a <= c:
    print(a)
elif b <= a and b <= c:
    print(b)
else:
    print(c)

######### leap year ######
year = 2024

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")


###simple intrest  ######
p = 10000
r = 5
t = 2

si = (p * r * t) / 100

print("Simple Interest =", si)

###### total and average ####
a = 80
b = 70
c = 90

total = a + b + c
average = total / 3

print("Total =", total)
print("Average =", average)

'''

































































































































































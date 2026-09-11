# 🐍 Python Operators

Operators are special symbols or keywords used to perform operations on values and variables in Python.

This section covers Python operators from **basic to advanced level** with examples and practical usage.

---

## 📌 Topics Covered

* Arithmetic Operators
* Assignment Operators
* Comparison Operators
* Logical Operators
* Identity Operators
* Membership Operators
* Bitwise Operators
* Operator Precedence

---

# 1️⃣ Arithmetic Operators

Arithmetic operators are used to perform mathematical calculations.

| Operator | Description    | Example   |
| -------- | -------------- | --------- |
| `+`      | Addition       | `10 + 5`  |
| `-`      | Subtraction    | `10 - 5`  |
| `*`      | Multiplication | `10 * 5`  |
| `/`      | Division       | `10 / 5`  |
| `//`     | Floor Division | `10 // 3` |
| `%`      | Modulus        | `10 % 3`  |
| `**`     | Exponentiation | `2 ** 3`  |

### Example

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

### Output

```text
13
7
30
3.3333333333333335
3
1
1000
```

---

# 2️⃣ Assignment Operators

Assignment operators are used to assign or update values in variables.

| Operator | Example   | Meaning      |
| -------- | --------- | ------------ |
| `=`      | `x = 10`  | Assign       |
| `+=`     | `x += 5`  | `x = x + 5`  |
| `-=`     | `x -= 5`  | `x = x - 5`  |
| `*=`     | `x *= 5`  | `x = x * 5`  |
| `/=`     | `x /= 5`  | `x = x / 5`  |
| `//=`    | `x //= 5` | `x = x // 5` |
| `%=`     | `x %= 5`  | `x = x % 5`  |
| `**=`    | `x **= 5` | `x = x ** 5` |

### Example

```python
x = 10

x += 5
print(x)

x *= 2
print(x)

x -= 5
print(x)
```

### Output

```text
15
30
25
```

---

# 3️⃣ Comparison Operators

Comparison operators compare two values and return either `True` or `False`.

| Operator | Description              |
| -------- | ------------------------ |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |

### Example

```python
a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
```

### Output

```text
False
True
False
True
False
True
```

---

# 4️⃣ Logical Operators

Logical operators are used to combine multiple conditions.

| Operator | Description                              |
| -------- | ---------------------------------------- |
| `and`    | True when both conditions are True       |
| `or`     | True when at least one condition is True |
| `not`    | Reverses the result                      |

### `and`

```python
age = 20
marks = 80

print(age >= 18 and marks >= 50)
```

Output:

```text
True
```

### `or`

```python
age = 16
marks = 80

print(age >= 18 or marks >= 50)
```

Output:

```text
True
```

### `not`

```python
x = 10

print(not(x > 5))
```

Output:

```text
False
```

---

# 5️⃣ Identity Operators

Identity operators check whether two variables refer to the **same object in memory**.

| Operator | Description       |
| -------- | ----------------- |
| `is`     | Same object       |
| `is not` | Different objects |

### Example

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)
print(a is c)
print(a is not c)
```

### Output

```text
True
False
True
```

### Important

`is` checks **object identity**, while `==` checks **value equality**.

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
```

Output:

```text
True
False
```

---

# 6️⃣ Membership Operators

Membership operators check whether a value exists inside a sequence such as a string, list, tuple, set, etc.

| Operator | Description          |
| -------- | -------------------- |
| `in`     | Value exists         |
| `not in` | Value does not exist |

### Example

```python
numbers = [10, 20, 30, 40]

print(20 in numbers)
print(50 in numbers)
print(50 not in numbers)
```

### Output

```text
True
False
True
```

### String Example

```python
name = "Python"

print("P" in name)
print("z" not in name)
```

Output:

```text
True
True
```

---

# 7️⃣ Bitwise Operators

Bitwise operators work directly with the binary representation of integers.

| Operator | Name        |    |
| -------- | ----------- | -- |
| `&`      | AND         |    |
| `        | `           | OR |
| `^`      | XOR         |    |
| `~`      | NOT         |    |
| `<<`     | Left Shift  |    |
| `>>`     | Right Shift |    |

### Example

```python
a = 5
b = 3

print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 1)
print(a >> 1)
```

### Output

```text
1
7
6
-6
10
2
```

### Binary Representation

```text
5 = 101
3 = 011
```

#### AND

```text
101
011
---
001 = 1
```

#### OR

```text
101
011
---
111 = 7
```

#### XOR

```text
101
011
---
110 = 6
```

---

# 8️⃣ Operator Precedence

When multiple operators appear in the same expression, Python follows a specific order of evaluation.

### Example

```python
result = 10 + 5 * 2
print(result)
```

Output:

```text
20
```

Multiplication is performed before addition:

```text
5 * 2 = 10
10 + 10 = 20
```

### Common Precedence Order

From higher to lower priority:

```text
()
**
+x, -x, ~x
*, /, //, %
+, -
<<, >>
&
^
|
<, <=, >, >=, ==, !=
not
and
or
```

### Example

```python
result = 10 + 2 * 5
print(result)
```

Output:

```text
20
```

Using parentheses:

```python
result = (10 + 2) * 5
print(result)
```

Output:

```text
60
```

---

# 🧠 Important Differences

### `=` vs `==`

```python
x = 10
```

`=` → assigns a value.

```python
x == 10
```

`==` → compares two values.

---

### `==` vs `is`

```python
==  → compares values
is  → compares object identity
```

---

### `/` vs `//`

```python
10 / 3
```

Output:

```text
3.3333333333333335
```

```python
10 // 3
```

Output:

```text
3
```

---

### `%` Operator

The `%` operator returns the remainder.

```python
10 % 3
```

Output:

```text
1
```

It is commonly used for:

* Checking even/odd numbers
* Divisibility
* Cyclic calculations

Example:

```python
number = 10

print(number % 2 == 0)
```

Output:

```text
True
```

---

# 🎯 Practical Applications

Operators are heavily used in:

* Conditional statements
* Loops
* Data validation
* Mathematical calculations
* Searching
* Sorting
* Algorithms
* Data Structures
* Competitive Programming
* LeetCode problems
* Data Analytics
* Real-world applications

---

# 💻 Practice Problems

### Beginner

1. Add two numbers.
2. Find the difference between two numbers.
3. Find the remainder of two numbers.
4. Check whether a number is even.
5. Check whether a number is divisible by 5.

### Intermediate

6. Calculate simple interest.
7. Calculate the average of three numbers.
8. Check whether a number lies between 10 and 100.
9. Check whether a person is eligible based on age and marks.
10. Calculate the final price after discount.

### Advanced

11. Find the largest of three numbers using comparison operators.
12. Check whether a number is divisible by both 3 and 5.
13. Check whether exactly one of two conditions is true.
14. Solve expressions using operator precedence.
15. Use bitwise operators to perform binary calculations.

---

# 📚 Learning Goals

After completing this section, I can:

* Understand all major Python operators.
* Perform mathematical calculations.
* Compare values.
* Combine multiple conditions.
* Check object identity.
* Check membership in collections.
* Understand basic bitwise operations.
* Apply operator precedence.
* Use operators in real-world programming problems.

---

## 🚀 Next Topic

### `02-If-Conditions`

In the next section, I will learn how operators are combined with conditions to make decisions in Python.

---

⭐ **Python Programming Journey — Basic → Intermediate → Advanced**

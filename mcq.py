#  What will the following code produce?
def test(x):
 return "Positive" if x > 0 else "Non-positive"
print(test(-0))
# A) Positive
# B) Non-positive //
# C) 0
#  D) SyntaxError

# 2. Identifiers
# Which of the following is a valid Python identifier?
# A) 3variable
# B) variable-name 
# C) _variable123 //
# D) continue

# 3. Variables and Assignment
# What will the output of the following code be?
x = 5
x += (x := 10)
print(x)
# A) 5
# B) 10
# C) 15 //
# D) 20

# 4. Data Types
# What is the type of the result of the following operation?
x = 4 / 2
print(type(x))
# A) int
# B) float //
# C) complex
# D) decimal.Decimal

# 5. Operators
# What will be the output of the following code?
x = 2
y = 5
print(x ** y // y ** x)
# A) 6 //
# B) 25
# C) 0
# D) 5

#6 What does the following expression evaluate to?
x = 3
y = 5
z = 7
result = x < y < z > x
print(result) 
# A) True //
# B) False
# C) None
# D) TypeError

#7  What will be the output of the following code?
x = [1, 2, 3]
y = x
y += [4, 5]
print(x)
# A) [1, 2, 3]
# B) [1, 2, 3, 4, 5] //
# C) Error
# D) [4, 5]

# 8. Boolean Operators
# What will be the output of the following code?
a = True
b = False
c = a or b and not a
print(c)
# A) True //
# B) False
# C) None
# D) SyntaxError

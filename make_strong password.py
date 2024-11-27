



# import re

# def check_password_strength(password):
#     # Check the length of the password
#     if len(password) < 8:
#         return "Weak"
    
#     # Check for at least one uppercase letter
#     if not re.search(r'[A-Z]', password):
#         return "Weak"
    
#     # Check for at least one lowercase letter
#     if not re.search(r'[a-z]', password):
#         return "Weak"
    
#     # Check for at least one digit
#     if not re.search(r'\d', password):
#         return "Weak"
    
#     # Check for at least one special character
#     if not re.search(r'[@#$%^&+=]', password):
#         return "Weak"
    
#     return "Strong"

# # Example usage:
# password = input("Enter your password: ")
# print(check_password_strength(password))


# def longest_palindrome(s):
#     longest = ""  # To store the longest palindrome
    
#     # Check each substring
#     for i in range(len(s)):
#         for j in range(i, len(s)):
#             substring = s[i:j+1]
        
#             if substring == substring[::-1]:
          
#                 if len(substring) > len(longest):
#                     longest = substring
#     return longest

# # Example usage:
# input_str = input("Enter a string: ")
# print(longest_palindrome(input_str))

# i=5
# while i>=0:
#  print("*"*i)
#  i-=1
# def sum_of_series(n):
#     # Initialize sum
#     total_sum = 0
    
#     # Loop through natural numbers from 1 to n and add the 4th power to total_sum
#     for i in range(1, n+1):
#         total_sum += i**4
    
#     return total_sum

# def is_palindrome(s):
#     s=s.lower().replace(" ","")

#     return s==s[::-1]
# print(is_palindrome("a man a plan a canal panama"))  
# 
# def add_numbers(*args):
#   total=sum(args)
#   print(f"The sum is {total}")

# add_numbers(1, 2, 3, 4  )
# def calculate_discount(price,discount):
#     return price (price ,discount)
# print(calculate_discount(100 discount-0.2)) 
# print(calculate_discount(100, 0.2))

# add =lambda x,y: x+y
# print(add(5,4))
# Example with list comprehension:

# numbers = [1, 2, 3, 4, 5]

# squares = [num** 2 for num in numbers]

# print(squares) # Output: [1, 4, 9, 16, 25



# Example without list comprehension:
# numbers = [1, 2, 3, 4, 5]

# squares = []

# for num in numbers:
#     squares.append(num ** 2)

# print(squares) # Output: (1, 4, 9, 16, 25)
# numbers =[1,2,3,4,5]
# squared =map(lambda x:x**2, numbers)
# print(list(squared))
# numbers =[1,2,3,4,5]
# even_number =filter(lambda x:x%2==0, numbers)
# print(list(even_number))


# silent
# listen
# def are_anagrams(str1, str2):  
#     str1 = str1.replace(" ", "").lower()  
#     str2 = str2.replace(" ", "").lower()  
    
    
#     return sorted(str1) == sorted(str2)  

 
# string1 = "Listen"  
# string2 = "Silent"  
# print(are_anagrams(string1, string2))




# def fibonacci(n):
#  if n <= 1:
#     return n
#  a, b = 0, 1 # Starting values: Fibonacci(0) = 0, Fibonacci(1) = 1 for in range(2, n + 1): -
#  for _ in range(2, n + 1):
#     a, b = b, a + b # Update values: 'a' becomes 'b', and 'b' becomes a
#  return b

# print(fibonacci(6))

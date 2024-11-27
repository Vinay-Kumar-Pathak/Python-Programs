



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
def sum_of_series(n):
    # Initialize sum
    total_sum = 0
    
    # Loop through natural numbers from 1 to n and add the 4th power to total_sum
    for i in range(1, n+1):
        total_sum += i**4
    
    return total_sum

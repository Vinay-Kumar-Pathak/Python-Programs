
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
def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Example usage:
input_str = input("Enter a string: ")
if is_palindrome(input_str):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
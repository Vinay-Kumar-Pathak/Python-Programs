# List of numbers
numbers = [66, 78, 79, 78, 66, 55, 44]

# Divisors
divisors = [2, 3, 4, 5]

# Check divisibility
for num in numbers:
    print(f"Number: {num}")
    divisible_by = [d for d in divisors if num % d == 0]
    
    if divisible_by:
        print(f"Divisible by: {divisible_by}")
    else:
        print("Not divisible by 2, 3, 4, or 5.")
    print()  # For better formatting
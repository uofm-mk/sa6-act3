# test case
number = 354

# Define a lambda function to compute the sum of digits
sum_of_digits = lambda x: sum(int(digit) for digit in str(x) if digit.isdigit())

# Compute the sum of digits using the lambda function
result = sum_of_digits(number)

# Print the result
print("Sum of digits:", result)
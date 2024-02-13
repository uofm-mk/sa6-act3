#Function to find max num in a list
def find_maximum(numbers, compare):
    #If the list contains non numbers return none
    if not numbers:
        return None

    maximum = numbers[0]
    for num in numbers[1:]:
        if compare(num, maximum) > 0:
            maximum = num
    return maximum

# Test case
numbers = [10, 5, 8, 20, 3, 15]
# Lambda function 
compare_func = lambda a, b: a if a > b else b
# Find the maximum by using find_maximum function
maximum = find_maximum(numbers, compare_func)
print("Maximum number:", maximum)

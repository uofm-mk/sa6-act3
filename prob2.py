# List of strings
strings = ["Lebron", "Kyrie", "Tyson", "Kobe", "Mason", "James", "Harrison", "Antonio"]

# Ascending order by length, tie break alphabetical
sorted_strings = sorted(strings, key=lambda x: (len(x), x))

# Print the sorted list
print("Sorted strings:", sorted_strings)
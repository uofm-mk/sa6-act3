# Test case
list1 = [12, 23, 33, 43, 53, 22]
list2 = [43, 53, 63, 73, 83, 12]

def intersection(list1, list2):
    # Use a lambda function to filter elements in both lists
    both = list(filter(lambda x: x in list1, list2))
    return both

both = intersection(list1, list2)
print("Intersection of the two lists:", both)
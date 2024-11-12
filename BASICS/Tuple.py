# tuples are immutable i.e we can't modify them like list.

numbers = (23, 54, 53, 34, 334, 32, 34)

# Operations on Tuples :-


# 1. Indexing -> This will print the index of the given element.

print(numbers[0])  # Output: 23
       #OR
print(numbers.index(23))

# 2. Count -> used to count the number of occurrences of the given element.

print(numbers.count(34))
name = "Arunesh Sharma"

print(name.upper())
print(name.lower())
print(name) # This proves that the original string is not changed. It is immutable.


# Find Operation :-
name = "Arunesh Sharma"
print(name.find('S'))
print(name.find('A')) # will print index and will return -1 if not found.
print(name.find("Sharma"))

# If we just want to check if the string or charachter is present in the string then we can use the in keyword.
print('S' in name)


# Update or Replace :-

name = "Arunesh Sharma"
print(name.replace("Arunesh", "Arun")) # This will replace the first occurrence of Arunesh
marks = [67, 34, 67, 44, 35]

print(marks[1]) # this will start from first element i.e. the element at index 0 and will print the element at index 1 which is 34.
print(marks[-1]) # this will start from last element i.e. the element at index -1 and will print the element at index -1 which is 35.

print(" ")

print(marks[0 : 2]) # this will create a new list containing the elements at index 0 and 1 which are 67 and 34. The element at index 2 is not included in the new list.

print(" ")



# Using loops with List :-

for points in marks:
    print(points) # this will start from first element i.e. the element at index 0 and will print the element
    

print(" ")



#Operations in List :-

# 1. Append -> Used to add a new element in the list at last index.

marks.append(80) # this will add a new element 80 at the end of the list.

print(marks)

print(" ")


# 2. Insert -> If we want to add an element at a specific index then we use insert method.

marks.insert(2, 55) # this will add a new element 55 at the 2nd index of the list.

print(marks)

print(" ")


# 3. Length -> If we want to print the length of the list.

print(len(marks)) 

print(" ")

# 4. Remove -> If we want to remove an element.

marks.remove(67) # this will remove the first occurrence of 67 from the list.

print(marks)

print(" ")


# Using While loop with List :-

i = 0

while i < len(marks): # we use length of the list to control the loop
    print(marks[i])
    i = i + 1
    
print(" ")
    
# 5. Clear -> useds to clear the list.

marks.clear() # this will clear the list.
print(marks)

print(" ")
numbers = [1, 2, 3, 4, 5, 6]

for num in numbers:
    if num == 3:
        break  # break means it will break the loop when if condition is satisfied.
    print(num) # therefore here,  output will be 1 and 2.
    
    
print("")


numbers2 = [1, 2, 3, 4, 5, 6]

for num2 in numbers2:
    if num2 == 3:
        continue  # continue means it will skip the current iteration and move to the next one.
    print(num2) # therefore here, output will be 1, 2, 4, 5, 6.
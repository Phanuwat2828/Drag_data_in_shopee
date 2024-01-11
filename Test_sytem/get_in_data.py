# install pip install openpyxl

# Creating a 2D array using nested lists
rows = 3
cols = 4

# Method 1: Using list comprehension
two_d_array = [[0 for j in range(cols)] for i in range(rows)]

# Method 2: Using nested loops
# two_d_array = []
# for i in range(rows):
#     row = [0 for j in range(cols)]
#     two_d_array.append(row)

# Accessing elements
two_d_array[1][2] = 42
print(two_d_array[1][2])  # Output: 42
import pdb

x = [1, 2, 3, "x"]
y = 2
z = 3
arr = [2, 4, 5, 7, "x"]
arr_2d = [[1, 2], [3, 4]]

print("The Array is: ", arr)  # printing the array
print("The 2D-Array is: ", arr_2d)  # printing the 2D-Array

result = y + z
print(result)

# Set a trace using Python Debugger
pdb.set_trace()

result2 = y + x[0]
print(result2)

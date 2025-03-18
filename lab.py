# 1. Two Sum // Leetcode
my_array = [2,7,11,15]
target = 9

# n at position 0
if my_array[0] + my_array[1] == target:
    print("Numbers match target, indices:")
    print([0,1])
elif my_array[0] + my_array[2] == target:
    print("Numbers match target, indices:")
    print([0,2])
elif my_array[0] + my_array[3] == target:
    print("Numbers match target, indices:")
    print([0,3])
# n at position 1
elif my_array[1] + my_array[2] == target:
    print("Numbers match target, indices:")
    print([1,2])
elif my_array[1] + my_array[3] == target:
    print("Numbers match target, indices:")
    print([1,3])
# n at position 2
elif my_array[2] + my_array[3] == target:
    print("Numbers match target, indices:")
    print([2,3])
else:
    print("No two integers matching target found")








my_list = [2,3,4,6,7]

my_list.append(0,4)




























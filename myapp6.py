total = 0
for i in range(1, 5):
    total += i
print(total)

total2 = 0
j = 1

while j < 5:
    total2 += j
    j += 1
print(total2)

given_list = [5, 4, 4, 3, 1, -2, -3, -5]
total3 = 0
i = 0
while i < len(given_list) and given_list[i] > 0:
    total3 += given_list[i]
    i += 1
print(total3)

given_list2 = [5, 4, 4, 3, 1, -2, -3, -5]
total4 = 0
for element in given_list2:
    if element <= 0:
        break
    total4 += element
print(total4)

# given_list2 = [5, 4, 4, 3, 1, -2, -3, -5]
total5 = 0
i = 0
while True:
    total5 += given_list2[i]
    i += 1
    if given_list[i] <= 0:
        break
print(total5)

# Task: add all negative numbers from list using only
# while and for loops.
given_list3 = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]
i = 0
total6 = 0
while i < len(given_list3):2\
    if given_list3[i] < 0:
        total6 += given_list3[i]
    i += 1
print(-abs(total6))
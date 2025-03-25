a = ["banana", "apple", "microsoft"]
print(a[0])
print(a[1])
print(a[2])

for element in a:
    print(element)
    print(element)

b = [20, 10, 5]
total = 0
for e in b:
    total = total + e


print(total)

c = list(range(1, 5))
print(c)

total2 = 0
for i in range(1,5):
    total2 += i
print(total2)

print(4%3)

print(5%3)

print(1%3)

print(6%3)

print(list(range(1,8)))
total3 = 0
for i in range(1,8):
    if i % 3 == 0:
        total3 += i

print(total3)

# Task: Can you compute all multiples of 3, 5
# that are less than 100?

print(list(range(1,100)))
for i in range(1,100):
    if i % 3 == 0:
        print(i)
    elif i % 5 == 0:
        print(i)
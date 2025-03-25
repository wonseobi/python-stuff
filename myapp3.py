# Functions | CS Dojo
#     a collection of instructions
#     a collection of code

def function1():
    print("ahh")
    print("ahh2")
print("this ias outside the function")

# a mapping
# input or an argument

def function2(x):
    return 2*x
a = function2(3)
print(a) # return value or output
b = function2(4)
print(b)
c = function2(5)
print(c)

def function3(x, y):
    return x+y
e = function3(1, 2)

def function4(x):
    print(x)
    print("still in this function")
    return 3*x
f = function4(4)
print(f)

def function5(some_argument):
    print(some_argument)
    print("foobar")

# BMI calculator
name1 = "Won"
height_m1 = 1.91
weight_kg1 = 85

name2 = "Won's sister"
height_m2 = 1.70
weight_kg2 = 70

name3 = "Won's other sister"
height_m3 = 1.60
weight_kg3 = 50

def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print("BMI: ")
    print(bmi)
    if bmi < 25:
        return name + " is not overweight"
    else:
        return name + " is overweight"


result1 = bmi_calculator(name1, height_m1, weight_kg1)
result2 = bmi_calculator(name2, height_m2, weight_kg2)
result3 = bmi_calculator(name3, height_m3, weight_kg3)

print(result1)
print(result2)
print(result3)

def convert(miles):
    kilometer = miles * 1.60934
    return kilometer

result4 = convert(100)
print(result4)
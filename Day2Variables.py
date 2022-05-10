# 'Day 2: 30 Days of python programming'

# Exercises: Level 1
from itertools import product
from math import remainder


first_name = 'Candiru'
last_name = 'joana'
full_name = 'Chuku devins'
country = 'Uganda'
city = 'Kampala'
age = 23
year = '1998'
is_married = True
is_true = False
is_light = False

first_name, last_name, full_name, country, city, age, year, is_married, is_true, is_light = 'Candiru','joana', 'Chuku devins', 'Uganda', 'Kampala', 23, '1998',True, False, False

# Exercises: Level 2
#Q1 Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light))

#Q2 Using the len() built-in function, find the length of your first name
print(len(first_name))

#Q3 Compare the length of your first name and your last name
print(len(first_name))
print(len(last_name))

#Q4 # Declare 5 as num_one and 4 as num_two
# Add num_one and num_two and assign the value to a variable total
num_one = 5
num_two = 4
total = num_one + num_two
print(total)

# Subtract num_two from num_one and assign the value to a variable diff
diff =num_two-num_one
print(diff)

# Multiply num_two and num_one and assign the value to a variable product
product =num_two*num_one
print(product)

# Divide num_one by num_two and assign the value to a variable division
division =num_two/num_one
print(division)

# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder =num_two%num_one
print(remainder)

# Calculate num_one to the power of num_two and assign the value to a variable exp
exp =num_two**num_one
print(exp)

# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division =num_two//num_one
print(floor_division)


# The radius of a circle is 30 meters.
radius = 30
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle =3.14*radius**2
print(area_of_circle)

# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle= 2*3.14*radius
print(circum_of_circle)

# Take radius as user input and calculate the area.
radius = int(input("Enter radius:"))
areaOfcircle =3.14*radius**2
print(areaOfcircle)

# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input("Enter firstname:")
print(first_name)
last_name = input("Enter lastname:")
print(last_name)
country = input("Enter country:")
print(country)
age= input("Enter age:")
print(age)

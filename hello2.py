
#this is a comment

"""""
 is multi line#
"""""
first_name="ALice"
user_age= 25
print(user_age)

total=10-7
power=10**2
print(power)

string="my name is dave"
my_long_string="""
my name is dave
ebbelar 
"""
print(my_long_string)

first_name="dave" 
last_name="ebbelar"
full_name= first_name + " "+ last_name

long_dash= "_" * 30
print(full_name)
print(long_dash)
len(full_name)

is_logged_in= True



age = 25
has_license = True
drunk = True
can_drive = age >= 16 and has_license and not drunk
print(can_drive)

score = 10
score += 5 
score *=5
print(score)

name=" dave"

name.lower()
name.upper()

sentence="hi my bna"
sentence.title() 

name="dave"
string= f"hi there my name is {name}"

temperature = 31
if temperature > 30:
    print(" its very hot")
elif temperature > 25 :
    print("Its hot!")
else:
    print("Its nice weather")

score = 85

if score >= 90:
    print("A - Excellent!")
elif score >= 80:
    print("B - Good job!")
elif score >= 70:
    print("C - Keep it up!")
else:
    print("F - Need improvement")

age = 12
has_license = True
if age >= 18 and has_license:
    print("you can drive")
else:
    print("you cannot drive")

has_ticket = False
age = 15

if has_ticket:
    if age >= 18:
        print("enjoy the movie")
    else:
        print("needs supervision")
else:
    print("pls buy a ticket")

    for i in range(5):
        print("hello")

    for i in range(1,6):
        print(i)

    for i in range(0,10,2):
        print(i)

age = 25
has_license = False
my_list = ["alice",25,age, True, has_license]
my_list[0] = "Dave"


my_list.append("alice")
my_list.remove("alice")
my_list.insert(1,"Alice")

person = {
    "name" : "Alice",
    "age" : 25,
    "city" : "New York"
}

person["name"] = "Dave"
person["license"] = True
del person["license"]

empty= ()
point = (3,5)
colors = ("red","green","blue")
colors[0]

empty_set = set()
numbers = {1,2,3,4,5}
fruits= set(["apple","banana","apple"])

scores = [85,90,85,92,90]
unique_scores = set(scores)

def greet():
    print("Hello")
    print("hello again")
    pass
greet()

def check_weather():
    temperature = 30
    if temperature > 25:
        print('its hot')
    else:
         print("its nice weather")

check_weather()

def greet_alice():
    print("hello alice")

def greet(name):
    print(f"hello {name}")
greet(name="Dave")
greet(name ="alice")

def greet(first_name,last_name):
    print(f"hello,{first_name}{last_name}")
greet("dave","  ebbelaar")
greet(first_name="dave",last_name="  ebbelaar")
greet(last_name="  ebbelaar",first_name="dave")

def greet(last_name, first_name="john"):
    print(f"hello,{first_name}{last_name}")
greet(last_name=" ebbelr")

def greet(first_name="john",last_name="doe"):
    print(f"hello,{first_name}{last_name}")
greet(last_name="dave")

def calculate_total(price, tax_rate, discount):
    tax = price * tax_rate
    final_price = price + tax - discount
    print(f"Total: ${final_price}")

calculate_total(100, 0.08 , 10 )

def calculate_total(price, tax_rate, discount):
    tax = price * tax_rate
    final_price = price + tax - discount
    print(f"Total: ${final_price}")

calculate_total(price=100, tax_rate= 0.08 , discount=10 )

discount=50
def calculate_total(price):
    tax_rate = 0.08
   # discount = 10
    tax = price * tax_rate
    final_price = price + tax - discount
    print(f"Total: ${final_price}")

calculate_total(price=100 )



def calculate_total(price,discount):
    tax_rate = 0.08
   # discount = 10
    tax = price * tax_rate
    final_price = price + tax - discount
    print(f"Total: ${final_price}")

calculate_total(price=100, discount=10 )

def add_print(a,b):
    print(a+b)
add_print(a=5,b=10)

def add_return(a,b):
    return a + b
result=add_return(a=5,b=10)
result+20

#//////
def add_print(a,b):
    print(a+b)
print_result=add_print(a=5,b=10)

def add_return(a,b):
    return a + b
result=add_return(a=5,b=10)
result+20


def calculate_area(width, height):
    area = width * height
    area = area * 1.05
    return area

# Store the returned value
room_area = calculate_area(10, 12)
print(f"Room size: {room_area} sq ft") 
 # Room size: 120 sq ft



 def double(number):
    return number * 2

# Store in variable
result = double(5)

# Use in expressions
total = double(5) + double(3)  # 10 + 6 = 16

# Pass to other functions
print(double(10))  # 20

# Use in conditions
if double(7) > 10:
    print("Big number!")

def double(number):
    return number * 2

def simple_function():
    numbers = [1,2,3,4,5]
    first_number= numbers [0]
    last_number = numbers [-1]
    return first_number, last_number

f,l= simple_function()
print(f)
print(l)

import math
math.sqrt(16)
from math import sqrt, pi

from math import sqrt,pi
sqrt(16)

import random
number = random.randint(1,10)
choice= random.choice(["a","b","c"])

import os as hi
current_dir = hi.getcwd()
print(current_dir)

import pandas as pd
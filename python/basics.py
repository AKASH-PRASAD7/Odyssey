print("Hello World!")

#import 

from module import display

display("hi from module")

# Object Types / Data Types

# - Number : 1234, 3.1415, 3+4j, 0b111, Decimal(), Fraction()
# - String : 'spam', "Bob's", b'a\x01c', u'sp\xc4m'
# - List : [1, [2, 'three'], 4.5], list(range(10))
# - Tuple : (1, 'spam', 4, 'U'), tuple('spam'), namedtuple
# - Dictionary : {'food': 'spam', 'taste': 'yum'}, dict(hours=10)

# - Set : set('abc'), {'a', 'b', 'c'}

# - File : open('eggs.txt'), open(r'C:\ham.bin', 'wb')

# - Boolean : True, False
# - None : None
# - Funtions, modules, classes

# - Advance: Decorators, Generators, Iterators, MetaProgramming

# Tuples vs List

# Tuple is immutable
# List is mutable

# tuple = (1, 2, 3)
# list = [1, 2, 3]

# tuple[0] = 10
# list[0] = 10

# print(tuple) # Error
# print(list) # 10

l1 = [1,2,3]
l2 = [1,2,3]
l3 = l1

l1 == l2 # True (Value comparison)
l1 is l2 # False (Memory location comparison)
l1 is l3 # True (Memory location comparison)


1 < 2 < 3 # True
1 < 2 and 2 < 3 # True


# String formatting

name = "Akash"
age = 21

# Old way
print("Name: %s, Age: %d" % (name, age))

# Better way
print("Name: {}, Age: {}".format(name, age))

# Best way (Python 3.6+)
print(f"Name: {name}, Age: {age}")

# String methods

name = "Akash"

print(len(name)) # Length of string
print(name.upper()) # Convert to uppercase
print(name.lower()) # Convert to lowercase
print(name[1:3]) # Slicing
print(name.capitalize()) # Capitalize first letter
print(name.swapcase()) # Swap case
print(name.replace("Akash", "John")) # Replace substring
print(name.split(",")) # Split by comma returns list
print(name.join(["Akash", "Cena"])) # Join list into string
print(name.find("Akash")) # Find index of substring
print(name.index("Akash")) # Find index of substring
print(name.count("a")) # Count occurrences of substring
print(name.strip()) # Remove whitespace
 
for i in name:
    print(i) # akash


# List

basket = ["apple", "banana", "cherry", "orange"]

for fruit in basket:
    print(fruit)

if "kiwi" in basket:
    print("kiwi is in the basket")
else:
    print("kiwi is not in the basket")

basket.append("kiwi")
print(basket) # ["apple", "banana", "cherry", "orange", "kiwi"]

basket.remove("kiwi")
print(basket) # ["apple", "banana", "cherry", "orange"]

basket.pop()
print(basket)    # ["apple", "banana", "cherry"]

basket.insert(1, "kiwi")
print(basket) # ["apple", "kiwi", "banana", "cherry"]

basket.sort()
print(basket) # ["apple", "banana", "cherry", "kiwi"]

newBasket = baset # reference
newBasket = basket[:] # deep copy
newBasket = basket.copy() # shallow copy

# List Comprehension

squares = [x**2 for x in range(10)]
print(squares) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# List Comprehension with condition

squares = [x**2 for x in range(10) if x % 2 == 0]
print(squares) # [0, 4, 16, 36, 64]

# List Comprehension with nested loops

squares = [x**2 for x in range(10) for y in range(10)]
print(squares) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# Dictionary

person = {"name": "John", "age": 30, "city": "New York"}

print(person["name"])

for key, value in person.items():
    print(key, value)

for key in person.keys():
    print(key)

for value in person.values():
    print(value)

if "name" in person:
    print("name is in the dictionary")
else:
    print("name is not in the dictionary")

squared = {x: x**2 for x in range(10)}
print(squared) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

dict.fromkeys(["name", "age", "city"], "unknown")
print(dict.fromkeys(["name", "age", "city"], "unknown")) # {'name': 'unknown', 'age': 'unknown', 'city': 'unknown'}


# Set

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))
print(set1.issubset(set2))
print(set1.issuperset(set2))
print(set1.isdisjoint(set2))


# Tuple

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)

print(tuple1.union(tuple2))
print(tuple1.intersection(tuple2))
print(tuple1.difference(tuple2))
print(tuple1.symmetric_difference(tuple2))
print(tuple1.issubset(tuple2))
print(tuple1.issuperset(tuple2))
print(tuple1.isdisjoint(tuple2))


# Itearables
  
__iter__() # returns iterator
__next__() # returns next item

iter() # returns iterator
next() # returns next item


# Functions
 
def add(a=1,b=2):
    return a+b

print(add())
print(add(2,3))


# Lambda Functions (Anonymous Functions)
# Use case: when you need a function for a short period of time

add = lambda a, b: a + b
print(add(1, 2))

def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))

# Kwargs

def sum_all(**kwargs):
    return sum(kwargs.values())

print(sum_all(a=1, b=2, c=3, d=4, e=5))

# Pass keyword: pass is used to skip a line or block of code

def add(a, b):
    pass

print(add(1, 2)) # None

# Generators

def fibonacci():
    a, b = 0, 1
    while True:
        yield a # Pauses the function and returns the value
        a, b = b, a + b

for i in fibonacci():
    print(i)
    if i > 100:
        break


# Closure

def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

outer_function("Hello")()
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

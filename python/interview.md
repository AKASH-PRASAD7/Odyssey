# Python interview Question

## 0. `__pycache__`, interpreated or compiled ?

-- `__pycache__` is a directory that is created by the Python interpreter
-- It contains the bytecode of the Python code

- Python is an interpreted language
- But it is also a compiled language
- Python code is first compiled into bytecode
- Then the bytecode is interpreted by the Python interpreter (PVM)
- The bytecode is stored in the `__pycache__` directory

```python
.py file
   ↓ (compile)
bytecode (.pyc)
   ↓ (PVM interprets)
execution output
```

## 1. `==` and `is`

- `==` checks for equality of value
- `is` checks for equality of reference (memory location)

```python
a = [1, 2]
b = [1, 2]

print(a == b) # True
print(a is b) # False
```

## 2. Shallow copy vs deep copy

- **Shallow copy** (`copy.copy`) — copies the object but **shares references** to nested objects.
- **Deep copy** (`copy.deepcopy`) — recursively copies **everything**, including nested objects.

```python
import copy

lst = [[1, 2], [3, 4]]
s = copy.copy(lst) # Shallow copy
s1 = lst # Assignemnt
s2 = lst[:] # Shallow copy (Using slicing)

d = copy.deepcopy(lst) # Deep copy


s[0][0] = 99  # also changes lst[0][0]
d[0][0] = 42  # does NOT change lst[0][0]
```

## 3. List Comprehension

- List comprehension is a concise way to create lists
- It is a shorthand for a `for` loop that creates a list

```python
squares = [x**2 for x in range(10)]
print(squares) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

- With condition

squares = [x**2 for x in range(10) if x % 2 == 0]
print(squares) # [0, 4, 16, 36, 64]
```

## 4. Iterators

- An object implementing `__iter__()` and `__next__()`. Raises `StopIteration` when exhausted.

```python
itr = iter([1, 2, 3])
print(next(itr))  # 1
print(next(itr))  # 2
print(next(itr))  # 3
# next(itr) → StopIteration
```

## 5. Generators

- Functions that use `yield` instead of `return` — a simpler way to create iterators.
- A generator is like a paused function that resumes where it left off

```python
def gen():
    yield 1
    yield 2

g = gen()
print(next(g))  # 1
print(next(g))  # 2
# next(g) → StopIteration
```

## 6. Lambda Functions

- Lambda functions are anonymous functions that can take any number of arguments but can only have one expression

```python
add = lambda a, b: a + b
print(add(1, 2)) # 3
```

## 7. *args and **kwargs

- `*args` - collects extra positional arguments into a tuple
- `**kwargs` - collects extra keyword arguments into a dictionary

```python
def func(*args, **kwargs):
    print(args)
    print(kwargs)

func(1, 2, 3, a=1, b=2, c=3)
# Output:
# (*args → (1, 2, 3), **kwargs → {'a': 1, 'b': 2, 'c': 3})
```

## 8. Decorators

- Decorators are functions that add functionality to other functions (like middleware)

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called")
        func(*args, **kwargs)
        print("Something is happening after the function is called")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

## 9. `__init__`, `self`, `__name__`, `__main__`

- `__init__` — constructor, runs when an object is created.
- `self` — reference to the current instance (convention, not a keyword).
- `__name__` — holds the module name; equals `"__main__"` when the file is run directly.

```python
class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        print(f"{self.name} says Woof!")

if __name__ == "__main__":
    Dog("Buddy").bark()  # Buddy says Woof!
```


## 10. Mutable and Immutable (Memory Level)

- **Mutable** — can be changed after creation (`list`, `dict`, `set`)
- **Immutable** — cannot be changed after creation (`int`, `float`, `str`, `tuple`)

```python
# Mutable
a = [1, 2, 3]
a[0] = 99        # ✅ works
print(a)          # [99, 2, 3]

# Immutable
b = "Hello"
b[0] = "J"        # ❌ TypeError: 'str' does not support item assignment
```


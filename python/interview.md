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

## 11. Context Managers — `with` statement

- Automatically handles **setup and cleanup** (e.g. closing files, releasing locks).
- Implements `__enter__()` and `__exit__()` under the hood.

```python
# Without context manager — must close manually
f = open("data.txt")
data = f.read()
f.close()

# With context manager — auto-closes even if an error occurs
with open("data.txt") as f:
    data = f.read()
```

Custom context manager using a class:

```python
class DBConnection:
    def __init__(self, db):
        self.db = db
    def __enter__(self):
        print(f"Connecting to {self.db}")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Connection closed")

with DBConnection("mydb") as conn:
    print("Running query")
# Output: Connecting to mydb → Running query → Connection closed
```

-- __init__ - constructor
-- __enter__ - setup (entering context)
-- __exit__ - cleanup (exiting context)

## 12. `try`, `except`, `else`, `finally`

- `try` — block where errors might occur.
- `except` — runs if an error occurs in `try`.
- `else` — runs if **no error** occurred in `try`.
- `finally` — **always** runs (error or no error).

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("No error occurred")
finally:
    print("Always runs")
```

## 13. Asynchronous Python - `async` and `await`

- `async` defines a coroutine (an async function).
- `await` pauses execution until the awaited coroutine completes, allowing the event loop to run other tasks.
- Ideal for **I/O-bound** code (network requests, database queries) to prevent blocking.

```python
import asyncio

async def fetch_data(delay):
    print(f"Fetching data after {delay} seconds...")
    await asyncio.sleep(delay)  # non-blocking pause
    return f"Data from {delay}s"

async def main():
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))
    
    result1 = await task1
    result2 = await task2
    print(result1, result2)

if __name__ == "__main__":
    asyncio.run(main()) # Event loop will run the coroutine
# Output runs concurrently, not one after the other
```

## 14. GIL (Global Interpreter Lock)

- GIL is a mutex that protects access to Python objects, preventing multiple threads from executing Python bytecode at the same time
- It is used to simplify memory management and prevent race conditions
- It is not a problem for CPU-bound tasks (only one thread at a time)
- It is a problem for I/O-bound tasks (multiple threads waiting for I/O)

## 15. Memory Management

- **Reference counting** — each object tracks how many references point to it; deleted when count hits 0.
- **Garbage collector** — detects and cleans up **circular references** that reference counting can't handle.
- **Memory pooling** — Python pre-allocates small objects (ints `-5` to `256`, short strings) for reuse.

```python
import sys

a = [1, 2, 3]
print(sys.getrefcount(a))  # reference count (includes the getrefcount arg itself)

del a  # decrements ref count → object freed when it reaches 0
```

## 16. `eval()` function

- Evaluates a **string as a Python expression** and returns the result.
- ⚠️ **Security risk** — never use on untrusted input.

```python
x = eval("2 + 3")   # 5

def cal(a, b, op):
    return eval(f'{a} {op} {b}')

print(cal(10, 5, '*')) # 50

# Safer alternative for data literals
import ast
ast.literal_eval("[1, 2, 3]")  # [1, 2, 3]
```

## 17. `map()`, `filter()`, `reduce()`

- **`map(fn, iterable)`** — applies `fn` to every item.
- **`filter(fn, iterable)`** — keeps items where `fn` returns `True`.
- **`reduce(fn, iterable)`** — cumulatively applies `fn` to reduce to a single value.

```python
from functools import reduce

nums = [1, 2, 3, 4, 5]

list(map(lambda x: x**2, nums))       # [1, 4, 9, 16, 25]
list(filter(lambda x: x > 2, nums))   # [3, 4, 5]
reduce(lambda a, b: a + b, nums)      # 15
```

## 18. `staticmethod` vs `classmethod`

- **`@staticmethod`** — no access to `self` or `cls`; just a utility function inside a class.
- **`@classmethod`** — receives `cls` as first arg; can access/modify class state.

```python
class Math:
    base = 10

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def add_to_base(cls, x):
        return cls.base + x

Math.add(2, 3)        # 5
Math.add_to_base(5)   # 15
```

## 19. `__str__` vs `__repr__`

- `__str__` — human-readable string (used by `print()`).
- `__repr__` — unambiguous developer string (used in REPL / debugging).

```python
class User:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
    def __repr__(self):
        return f"User('{self.name}')"

u = User("Alice")
print(u)     # Alice        (__str__)
repr(u)      # User('Alice') (__repr__)
```

## 20. Multithreading vs Multiprocessing

- **Threading** (`threading`) — concurrent, shares memory, limited by GIL → best for **I/O-bound** tasks.
- **Multiprocessing** (`multiprocessing`) — parallel, separate memory, bypasses GIL → best for **CPU-bound** tasks.

```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# I/O-bound → threads
with ThreadPoolExecutor() as pool:
    results = pool.map(fetch_url, urls)

# CPU-bound → processes
with ProcessPoolExecutor() as pool:
    results = pool.map(heavy_compute, data)
```

## 21. PEP 8

- **PEP 8** — official style guide for Python code

```python
# imports - always at the top
import os
from math import sqrt

# class names - PascalCase
class MyClass:
    # method names, variables - snake_case
    def my_method(self, arg):
        x = 10
```

## 22. Type Hinting

- Type hints provide optional type annotations that improve code readability and allow static analysis tools to catch type errors.
- Type hints are not enforced at runtime by default, but they can be checked using tools like `mypy`.

```python
from typing import List, Dict, Optional

# Function with type hints
def greet(name: str) -> str:
    return f"Hello, {name}"

# Function with optional arguments
def divide(a: float, b: float) -> Optional[float]:
    if b == 0:
        return None
    return a / b

# Function with list and dictionary hints
def process_data(data: List[Dict[str, int]]) -> List[str]:
    return [str(item['id']) for item in data]

# Type checking with mypy
# mypy example.py
# This would catch type errors before runtime
```

## 23. Virtual Environment

- **Virtual environment** — isolated Python environment that contains its own set of libraries and dependencies.
- **`venv`** — built-in module for creating virtual environments.
- **`pip`** — package installer for Python.

```python
# Create a virtual environment
python -m venv .venv

# On macOS and Linux
source .venv/bin/activate
```
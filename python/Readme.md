# 🐍 Python’s Inner Working 

## 📌 Overview Flow


```
[ Python Source Code (.py) ]
            ↓
        (Compiled)
            ↓
[ Byte Code (.pyc) ]
            ↓
[ Python Virtual Machine (PVM) ]
            ↓
          Output
```


* You write code in `.py` files
* Python converts it into **Byte Code**
* Byte code runs on the **Python Virtual Machine (PVM)**

---

## 🔁 Step 1: Compilation to Byte Code

```
[ .py File ]  ──▶  [ Byte Code ]
```
### ✨ Key Points:

* Byte code is:

  * Low-level (closer to machine)
  * Platform-independent 🌍
* Makes execution faster ⚡
* Mostly hidden from the user

---

## 📦 Byte Code Files

* Stored as: `.pyc` files
* Located in: `__pycache__/`

### 🧾 Example:

```
hello_chai.cpython-310.pyc
```

### 🧠 Important Notes:

* Generated **automatically**
* Depends on:

  * Source code changes
  * Python version
* Created mainly for **imported modules**
* ❌ Not created for top-level scripts (in most cases)

---

## ⚙️ Step 2: Python Virtual Machine (PVM)

```
[ Byte Code ]  ──▶  [ PVM ]  ──▶  [ Execution ]
```

### 🧩 What is PVM?

* A **runtime engine**
* Executes byte code line-by-line (loop)
* Also known as the **Python Interpreter**

---

## 🚫 Byte Code ≠ Machine Code

| Feature   | Byte Code    | Machine Code      |
| --------- | ------------ | ----------------- |
| Level     | Intermediate | Low-level         |
| Platform  | Independent  | Platform-specific |
| Execution | Via PVM      | Direct CPU        |

👉 Byte code needs Python to run — it's not directly understood by hardware.

---

## 🧪 Python Implementations

Different ways Python can run:

* **CPython** ⭐ (Standard implementation)
* **Jython** (Runs on Java Virtual Machine)
* **IronPython** (.NET framework)
* **Stackless Python** (Microthreading support)
* **PyPy** (Faster via JIT compilation)

---

## 🧠 Full Picture

```
Write Code (.py)
        ↓
     Compile
        ↓
Byte Code (.pyc)
        ↓
Stored in __pycache__
        ↓
Run via PVM
        ↓
     Output
```
---

## 🎯 Quick Summary

* Python is **both compiled + interpreted**
* `.py` → compiled to **byte code**
* Byte code → executed by **PVM**
* `.pyc` files improve performance
* PVM is the **engine behind execution**


# Mutable vs Immutable

## Mutable

* Can be changed (in memory)
* Examples: list, dict, set

## Immutable

* Cannot be changed (in memory)
* Examples: int, float, str, tuple

# Important Notes

* Varibles in python are just name tags they don't have data types
 where as objects(memory location) have data types 



| Function  | Purpose                    | Output for `"hello"` |
| --------- | -------------------------- | -------------------- |
| `repr()`  | Debugging / developer view | `'hello'`            |
| `str()`   | User-friendly display      | `hello`              |
| `print()` | Display to console         | `hello`              |



#  Python Cheatsheet

## Core Concepts
- Variables: `x = 10` (dynamic typing)
- Data types: `int`, `float`, `str`, `list`, `dict`, `tuple`, `set`
- Control flow: `if`, `elif`, `else`, `for`, `while`
- Functions: `def my_func(arg): return arg`
- Classes: `class MyClass:` with `__init__` and methods
- Error handling: `try`, `except`, `finally`, `raise`
- Modules: `import math`, `from os import path`

---

## String Methods
| Method | Example | Output |
|--------|---------|--------|
| `upper()` | `"hello".upper()` | `"HELLO"` |
| `lower()` | `"HELLO".lower()` | `"hello"` |
| `title()` | `"hello world".title()` | `"Hello World"` |
| `strip()` | `"  hi  ".strip()` | `"hi"` |
| `replace(a,b)` | `"hi hi".replace("hi","bye")` | `"bye bye"` |
| `split()` | `"a,b,c".split(",")` | `['a','b','c']` |
| `join(list)` | `",".join(['a','b'])` | `"a,b"` |
| `find()` | `"hello".find("e")` | `1` |
| `startswith()` | `"hello".startswith("he")` | `True` |
| `endswith()` | `"hello".endswith("lo")` | `True` |

---

## List Methods
| Method | Example | Output |
|--------|---------|--------|
| `append(x)` | `[1,2].append(3)` | `[1,2,3]` |
| `extend(iterable)` | `[1].extend([2,3])` | `[1,2,3]` |
| `insert(i,x)` | `[1,3].insert(1,2)` | `[1,2,3]` |
| `remove(x)` | `[1,2,2].remove(2)` | `[1,2]` |
| `pop(i)` | `[1,2,3].pop(1)` | `[1,3]` |
| `index(x)` | `[1,2,3].index(2)` | `1` |
| `count(x)` | `[1,2,2].count(2)` | `2` |
| `sort()` | `[3,1,2].sort()` | `[1,2,3]` |
| `reverse()` | `[1,2].reverse()` | `[2,1]` |
| `copy()` | `a = [1,2]; b = a.copy()` | `[1,2]` |

---

## Dictionary Methods
| Method | Example | Output |
|--------|---------|--------|
| `keys()` | `{"a":1,"b":2}.keys()` | `dict_keys(['a','b'])` |
| `values()` | `{"a":1,"b":2}.values()` | `dict_values([1,2])` |
| `items()` | `{"a":1}.items()` | `[('a',1)]` |
| `get(key)` | `{"a":1}.get("b")` | `None` |
| `update({...})` | `{"a":1}.update({"b":2})` | `{"a":1,"b":2}` |
| `pop(key)` | `{"a":1,"b":2}.pop("a")` | `{"b":2}` |
| `popitem()` | `{"a":1,"b":2}.popitem()` | removes `"b":2` |
| `clear()` | `{"a":1}.clear()` | `{}` |
| `copy()` | `d2 = d1.copy()` | `{"a":1}` |
| `setdefault(k,v)` | `{"a":1}.setdefault("b",2)` | `{"a":1,"b":2}` |

---



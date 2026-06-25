# OOP_exercises
Some of my solutions to exercises from my Data Science course, focused on writing clean, idiomatic Python using OOP. 

## Topics covered
- **Python data model (dunder methods):** custom container types, context managers
- **Validation and error handling:** raising appropiate exceptions
## Files
- `smart_warehouse.py` — a container class using `__getitem__`,
  `__setitem__`, `__delitem__` and `__contains__`, with stock-limit
  validation and automatic removal of zero-stock items.
- `context_manager.py` — a class implementing the context manager
  protocol (`__enter__` / `__exit__`).
  ## Requirements

  Python 3.10+

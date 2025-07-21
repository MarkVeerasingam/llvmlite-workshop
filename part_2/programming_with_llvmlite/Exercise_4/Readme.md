# Exercise 4: Structured Control Flow (SCF) and Single Static Assignment (SSA)
- 1) Write a JIT in Python that compiles the LLVM IR you generated for max_func.
- 2) Extend that JIT by adding another function to the module, for example, min_func(a, b) which returns the smaller of two integers.
- 3) Compile and run both functions via JIT, calling them from Python.

Here you will cover
- Structured Control Flow (SCF) — i.e., conditional branching (like an if).
- Static Single Assignment (SSA) form — with phi nodes to merge values from two paths.

Look at part_1 -> what_is_llvm -> part_1_theory

exercise_1.py builds a function like this in Python logic:

```
def max_func(a: int, b: int) -> int:
    if a > b:
        return a
    else:
        return b
```

# 1. Add a new function to your LLVM IR module.
Add a new function to your LLVM IR module:
Similar to max_func, create a min_func with this logic:

```
def min_func(a: int, b: int) -> int:
    if a < b:
        return a
    else:
        return b
```

# 2.Extend your JIT code
- You are going to be creating your own jit for this. This can be copied over from previous examples
- After compiling the IR, get the pointer to min_func as well.
- Wrap it with ctypes just like max_func.
- Test both functions from Python.
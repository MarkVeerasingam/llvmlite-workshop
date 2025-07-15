# Exercise 1 - Fix the Operation:

This piece of code has 2 things wrong. I want you to identify what they are...

## Problem 1:
Inside mul_ir.py, check the what type of data we are multiplying. We declare that we expect int 32 as an argument. However is that what we are multiplying.

## Problem 2:
Great you fixed problem 1. However, you might expect to see the output ```Segmentation fault (core dumped)``` 
This is expected. Inside run_jit.py, you will find that the issue is with how we are getting the pointer to the compiled function. Hint, look at the naming we called the function inside mul_ir.py and what we are naming it.

### Recommended Documentation:
- Example—defining a simple function: https://llvmlite.readthedocs.io/en/latest/user-guide/ir/examples.html
- 

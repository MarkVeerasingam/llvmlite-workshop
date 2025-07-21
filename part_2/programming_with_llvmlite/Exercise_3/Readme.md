# Exercise 3 - Running Handwritten IR with llvmlite.binding

## Goal: Try extending square_ir.ll by writing a second function:

Even though we haven’t fully covered LLVM IR syntax yet, this exercise invites you to experiment by writing a new IR function manually and using llvmlite.binding to execute.

It’s a great opportunity to begin thinking like a compiler and get familiar with LLVM’s low-level, typed, single-assignment format.

- square_ir.ll, contains a function that squares an integer.
- - This mimics the logic of a basic C function:
- - ``int square(int x) {
    return x * x;
}``

## The Task
-  Write a second function in the same file (or a new one), called cube, which calculates the cube of a number
- - ``int cube(int x) {
    return x * x * x;
}``
- LLVM IR Hint:
- - Within the entry block, you want to follow what is called single static assignment (SSA) - we will cover this in Part 3. 
- - In SSA, every variable is assigned exactly once, and each variable is uniquely named. This helps LLVM (and compilers in general) reason about the program more effectively for optimizations like dead code elimination, constant folding, and more.
- - When you are adding the cube IR, after the entry block you will need to assign something like 

```
%b = mul i32 %a %a
%c = mul i32 %b %a
```
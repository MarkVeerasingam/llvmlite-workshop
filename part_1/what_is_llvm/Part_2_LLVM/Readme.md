# What is LLVM?

This folder is part of the onboarding workshop to help you get comfortable with how LLVM works — before we dive into using `llvmlite`.

---

## TL;DR: What is LLVM?

LLVM is like a **toolkit for building compilers**.

Imagine you want to write a program in Python, C, or Rust, and then have it run on a real machine (like x86, ARM, or IBM’s Mainframe s390x). A compiler helps translate that high-level code into machine code your CPU understands. LLVM helps with that translation.

You can think of it like this:

```
High-level language (C, Rust, Python) -> LLVM IR -> Machine Code (x86, ARM, s390x)
```

# Question:

Before your code runs on a real CPU, it gets translated into what is called “Intermediate Representation” (IR). Why do you think compilers don’t translate directly from your code straight to machine code? Why have this middle step?

## What Is LLVM IR?

LLVM IR is like a universal high level “assembly language” that is:
- Portable across hardware (CPU/GPU/TPU)
- Easier for the compiler to analyze and improve -> leading to better optimizations
- Machine-independent (until the final step)

This IR lets the compiler be split into parts:
- Frontends (which convert source code to IR)
- Backends (which convert IR to machine code)

[11.2.5 Optimization and Code Generation - MIT OpenCourseWare](https://www.youtube.com/watch?v=e8eEyYmLx98)

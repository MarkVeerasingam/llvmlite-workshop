; ModuleID = "example_module"               ; name of the llvm module. This of this a source file or translation unit
target triple = "unknown-unknown-unknown"   ; the target archicture (x86, ARM, s390x, aarch64, GPU, etc...) 
target datalayout = ""                      ; describes memory layout details for the target.

define i32 @main() {                        ; Defines a function named 'main' that returns a 32-bit integer (i32)
entry:                                      ; The entry point label for this function (a basic block)
  ret i32 42                                ; Return the integer constant 42 from the function
}

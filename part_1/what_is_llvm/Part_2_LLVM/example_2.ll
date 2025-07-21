; ModuleID = "example_module"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @double(i32 %x) {         ; Function named 'double' that takes one i32 argument
entry:                               ; Entry basic block
  %result = mul i32 %x, 2            ; Multiply the input %x by 2 and store in %result
  ret i32 %result                    ; Return the result
}

; ModuleID = "control_flow_example"
target triple = "unknown-unknown-unknown"
target datalayout = ""

; Using the LLVM documentation, figure out what this code is doing
; LLVM Language Reference Manual : https://llvm.org/docs/LangRef.html

; Hint: Look back at Part_1_Theory. This piece of code is very similar.

define i32 @check_sign(i32 %x) {
entry:
  %is_positive = icmp sgt i32 %x, 0         
  br i1 %is_positive, label %positive, label %nonpositive  

positive:                                    
  ret i32 1

nonpositive:                                 
  ret i32 0
}

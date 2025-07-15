; ModuleID = 'square_module'
target triple = "unknown-unknown-unknown"
define i32 @square(i32 %x) {
entry:
  %result = mul i32 %x, %x
  ret i32 %result
}
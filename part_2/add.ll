; ModuleID = "add_module"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"add"(i32 %"x", i32 %"y")
{
entry:
  %"sum" = add i32 %"x", %"y"
  ret i32 %"sum"
}

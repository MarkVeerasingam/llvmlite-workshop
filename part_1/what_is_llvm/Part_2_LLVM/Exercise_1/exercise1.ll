; ModuleID = "add_module"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"add"(i32 %"a", i32 %"b")
{
entry:
  %"sum" = add i32 %"a", %"b"
  ret i32 %"sum"
}
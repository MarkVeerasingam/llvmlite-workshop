import os
from llvmlite import ir

# Create LLVM module and function
module = ir.Module(name="multiply_module")
func_ty = ir.FunctionType(ir.IntType(32), [ir.IntType(32), ir.IntType(32)])
function = ir.Function(module, func_ty, name="multiply")

# Name function arguments
x, y = function.args
x.name = "x"
y.name = "y"

# Create entry block and builder
block = function.append_basic_block(name="entry")
builder = ir.IRBuilder(block)

# Add instruction
"""
Hint:
This is where issue 1 is.
Look at the method that builder is calling, is it performing the correct multiplication we need for our expected input data types?
"""
result = builder.fmul(x, y, name="sum")
builder.ret(result)

# Get current directory of the script
current_dir = os.path.dirname(os.path.abspath(__file__))
ll_path = os.path.join(current_dir, "mul.ll")

# Output IR 
with open(ll_path, "w") as f:
    f.write(str(module))

print(f"LLVM IR written to {ll_path}")

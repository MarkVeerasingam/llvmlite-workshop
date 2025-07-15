import os
from llvmlite import ir

# Create LLVM module and function
module = ir.Module(name="mixed_multiply_module")

"""
Function type: float multiply(int a, float b)
Return type: float
"""
func_mixed_mul = ir.FunctionType(ir.FloatType(), [ir.IntType(32), ir.FloatType()])
function = ir.Function(module, func_mixed_mul, name="mixed_multiply")

# Name the arguments
int_arg, float_arg = function.args
int_arg.name = "a"
float_arg.name = "b"

# Create entry block and IR builder
block = function.append_basic_block(name="entry")
builder = ir.IRBuilder(block)

"""
# TODO:
- 1) Convert int32 to float (float type to match multiplication type)
- 2) Then multiply using fmul

- Hint: use builder.sitofp() to convert signed int to float

- Hint: within the function sitofp(), you will see various arguments. Remember that the integer we are converting to float is the LHS, int_arg. 
- So we need to tell sitofp() that the value is int_arg and typ to be of Float IR.
-> value: Any,
    typ: Any,
    name: str = ''
"""

# ** YOUR CODE GOES HERE **

# Write IR to file
current_dir = os.path.dirname(os.path.abspath(__file__))
ll_path = os.path.join(current_dir, "mixed_mul.ll")

with open(ll_path, "w") as f:
    f.write(str(module))

print(f"LLVM IR written to {ll_path}")

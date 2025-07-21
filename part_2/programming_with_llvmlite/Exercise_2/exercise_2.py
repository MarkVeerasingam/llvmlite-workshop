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
- 1) Convert int32 to float 
- 2) Then multiply using fmul
- 3) return builder.ret(result)

- Hint: use builder.sitofp() to convert signed int to float
-- sitofp() == Signed Integer to Floating point

- Hint: within the function sitofp(), you will see various arguments. Remember that the integer we are converting to float is on the Left-Hand-Side (LHS), line 11. 
- So we need to tell sitofp() that the value is int_arg and typ to be of Float IR.
-> value: Any,
    typ: Any,
    name: str = ''

# Note:
Function type: float multiply(int a, float b)
- We are converting int a to float. So we are doing int32
"""

# ** YOUR CODE GOES HERE **

# 1. Convert the int32 argument to float

# 2. Multiply the converted float with the float argument

# 3. Return the result

# Write IR to file
current_dir = os.path.dirname(os.path.abspath(__file__))
ll_path = os.path.join(current_dir, "mixed_mul.ll")

with open(ll_path, "w") as f:
    f.write(str(module))

print(f"LLVM IR written to {ll_path}")

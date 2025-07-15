from llvmlite import ir

# Create an LLVM module (think of this as a translation unit) 
module = ir.Module(name="add_module")

# Define the function type: int add(int a, int b)
# an easier way to understand this is as... 
# ir.FunctionType(return_type, [arg_type1, arg_type2, ...])
# in C this looks like... int add(int a, int b);
func_type = ir.FunctionType(ir.IntType(32), [ir.IntType(32), ir.IntType(32)])

# Create the function and give it a name
# in python this means "add_func" is a function where it holds the module and "func_type" we declared above.
add_func = ir.Function(module, func_type, name="add")

# Name the arguments for readability
a, b = add_func.args
a.name = "a"
b.name = "b"

# Create a block (basic block = single-entry, single-exit section of code)
entry_block = add_func.append_basic_block(name="entry")
builder = ir.IRBuilder(entry_block)

# Emit the add instruction
result = builder.add(a, b, name="sum")

# Return the result
builder.ret(result)

# Print out the LLVM IR
print(module)

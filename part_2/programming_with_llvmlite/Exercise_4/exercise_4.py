from llvmlite import ir
import os

# Create a new LLVM module to hold the function
module = ir.Module(name="ssa_branch_example")

# Define the function type: int max_func(int a, int b)
func_type = ir.FunctionType(ir.IntType(32), [ir.IntType(32), ir.IntType(32)])
func = ir.Function(module, func_type, name="max_func")

# Name the input arguments for readability
a, b = func.args
a.name = "a"
b.name = "b"

# Define basic blocks: entry, then, else, and merge
entry_block = func.append_basic_block("entry")
then_block = func.append_basic_block("then")
else_block = func.append_basic_block("else")
merge_block = func.append_basic_block("merge")

# Start building in the entry block
builder = ir.IRBuilder(entry_block)

# Compare: if a > b
cmp = builder.icmp_signed(">", a, b, name="cmp")

# Conditional branch: if true, go to 'then'; else, go to 'else'
builder.cbranch(cmp, then_block, else_block)

# THEN block: if a > b, this block runs
builder.position_at_start(then_block)
then_val = a  # result = a
builder.branch(merge_block)  # jump to merge block

# ELSE block: if a <= b, this block runs
builder.position_at_start(else_block)
else_val = b  # result = b
builder.branch(merge_block)  # jump to merge block

# MERGE block: SSA with a phi node to unify control flow
builder.position_at_start(merge_block)
result = builder.phi(ir.IntType(32), name="result")

# Register which values came from which block
result.add_incoming(then_val, then_block)
result.add_incoming(else_val, else_block)

# Return the selected result
builder.ret(result)

# Write the final IR to a file
ll_path = os.path.join(os.path.dirname(__file__), "ssa_max.ll")
with open(ll_path, "w") as f:
    f.write(str(module))

print(f"LLVM IR written to {ll_path}")

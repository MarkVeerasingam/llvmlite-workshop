import os
import llvmlite.binding as llvm
import ctypes

# Path to the .ll file 
current_dir = os.path.dirname(os.path.abspath(__file__))
ll_path = os.path.join(current_dir, "mul.ll")

# Initialize LLVM
llvm.initialize()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()

# Load IR
with open(ll_path) as f:
    llvm_ir = f.read()

# Create JIT engine
def create_execution_engine():
    target = llvm.Target.from_default_triple()
    target_machine = target.create_target_machine()
    backing_mod = llvm.parse_assembly("")
    engine = llvm.create_mcjit_compiler(backing_mod, target_machine)
    return engine

# Compile IR
def compile_ir(engine, llvm_ir):
    mod = llvm.parse_assembly(llvm_ir)
    mod.verify()
    engine.add_module(mod)
    engine.finalize_object()
    return mod

engine = create_execution_engine()
mod = compile_ir(engine, llvm_ir)

# Get pointer to compiled 'multiply' function
"""
Hint:
This is where we are getting the pointer to the compiled function. Check the naming of this and what we called the name of the function inside mul_ir.py
"""
func_ptr = engine.get_function_address("mul")

# Convert to callable using ctypes
cfunc = ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.c_int32, ctypes.c_int32)(func_ptr)

# Call function
result = cfunc(7, 5)
print("mul(7, 5) =", result)

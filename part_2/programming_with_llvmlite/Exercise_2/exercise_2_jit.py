import os
import llvmlite.binding as llvm
import ctypes

# Path to the .ll file 
current_dir = os.path.dirname(os.path.abspath(__file__))
ll_path = os.path.join(current_dir, "mixed_mul.ll")

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

# Get pointer to compiled function
func_ptr = engine.get_function_address("mixed_multiply")

# Convert to callable using ctypes
# ctypes.c_int32 (int), ctypes.c_float (float) -> ctypes.c_float (return)
cfunc = ctypes.CFUNCTYPE(ctypes.c_float, ctypes.c_int32, ctypes.c_float)(func_ptr)

# Call function
arg_a = 5
arg_b = 2.5
result = cfunc(arg_a, arg_b)
print(f"mixed_multiply({arg_a}, {arg_b}) = {result}")

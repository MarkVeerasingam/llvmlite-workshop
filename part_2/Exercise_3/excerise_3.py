import os
import llvmlite.binding as llvm
import ctypes

# read in llvm file
current_dir = os.path.dirname(os.path.abspath(__file__))
ll_path = os.path.join(current_dir, "square_ir.ll")
with open(ll_path) as f:
    llvm_ir = f.read()

# === LLVM Initialization ===
llvm.initialize()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()

# Create a JIT execution engine
def create_execution_engine():
    target = llvm.Target.from_default_triple()
    target_machine = target.create_target_machine()
    backing_mod = llvm.parse_assembly("")
    engine = llvm.create_mcjit_compiler(backing_mod, target_machine)
    return engine

# Compile the IR
def compile_ir(engine, llvm_ir):
    mod = llvm.parse_assembly(llvm_ir)
    mod.verify()
    engine.add_module(mod)
    engine.finalize_object()
    return mod

# Run setup
engine = create_execution_engine()
mod = compile_ir(engine, llvm_ir)

# === Get function pointers and wrap with ctypes ===

# === Square === #
# Get function pointer to 'square'
square_ptr = engine.get_function_address("square")

# Convert to callable Python function
c_square = ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.c_int32)(square_ptr)

# === Cube === #
# == Your Code Goes Here == #

# === Test ===
x = 4
print(f"square({x}) = {c_square(x)}")  # Output: square(4) = 16

# Remember to test for Cube too!
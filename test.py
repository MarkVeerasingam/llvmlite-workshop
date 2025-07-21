import llvmlite.binding as llvm

# Initialize LLVM components
llvm.initialize()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()

# Get the native target triple (like x86_64-pc-linux-gnu)
target_triple = llvm.get_default_triple()
print("Target triple:", target_triple)


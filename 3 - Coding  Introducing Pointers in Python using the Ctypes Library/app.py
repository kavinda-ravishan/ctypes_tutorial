import ctypes

clib = ctypes.CDLL("./clib.so")

# example 1
alloc_memory = clib.alloc_memory
alloc_memory.argtypes = ()
alloc_memory.restype = ctypes.POINTER(ctypes.c_char_p)

free_memory = clib.free_memory
free_memory.argtypes = (ctypes.POINTER(ctypes.c_char_p), )
free_memory.restype = None

addr = alloc_memory()
print(addr)

cstring = ctypes.c_char_p.from_buffer(addr)
print(cstring.value.decode("utf-8"))

free_memory(addr)

# example 2
# ctypes.pointer(obj)
# This function creates a new pointer instance, pointing to obj. The returned object is of the type POINTER(type(obj)).
# Note: If you just want to pass a pointer to an object to a foreign function call, you should use byref(obj) which is much faster.
num = ctypes.c_int(123)

ptr = ctypes.pointer(num)
print(ptr.contents)

# ctypes.POINTER(type)
# This factory function creates and returns a new ctypes pointer type.
# Pointer types are cached and reused internally, so calling this function repeatedly is cheap.
# type must be a ctypes type.
ptr = ctypes.POINTER(ctypes.c_int)
ptr.contents = num
print(ptr.contents)
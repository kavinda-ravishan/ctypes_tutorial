import ctypes, os

cwd_path = os.getcwd()
lib_name = "clib.so"
clib = ctypes.CDLL(os.path.join(cwd_path, lib_name))

# example 1
arr_size = 10
arr = (ctypes.c_int32 * arr_size)()

for i in range(len(arr)):
    print(arr[i], end=" ")
print()

init_arr = clib.init_arr
init_arr.argtypes = (ctypes.POINTER(ctypes.c_int32), ctypes.c_uint32)
init_arr.restype = None

init_arr(arr, arr_size)

for i in range(len(arr)):
    print(arr[i], end=" ")
print()

# example 2
arr_size = 10

get_array = clib.get_array
get_array.argtypes = (ctypes.c_uint32, )
get_array.restype = ctypes.POINTER(ctypes.c_int32)

free_array = clib.free_array
free_array.argtypes = (ctypes.POINTER(ctypes.c_int32), )
free_array.restype = None

arr = get_array(arr_size)

for i in range(arr_size):
    print(arr[i], end=" ")
print()

free_array(arr)
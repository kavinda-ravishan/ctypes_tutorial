import ctypes

clib = ctypes.CDLL("./clib.so")

# example 1
add = clib.add
add.argtypes = [ctypes.c_int, ctypes.c_int]
add.restype = ctypes.c_int

results = add(1, 2)

print(results)

# example 2
display = clib.display
display.argtypes = [ctypes.c_char_p]

display(b"hello from python\n")

string = ctypes.c_char_p(b"hello from python\n")
display(string)

print(f'string value : {string.value}')

print(f'Char pointer : {string}')
string.value = b"String updated"
print(f'Char pointer : {string}') # pointer value is changed

# example 3
string = ctypes.create_string_buffer(50)
string.value = b"string for buffer\n"
print(string.value)

print(f'Char pointer : {string}')
string.value = b"String updated"
print(f'Char pointer : {string}') # pointer value not changed
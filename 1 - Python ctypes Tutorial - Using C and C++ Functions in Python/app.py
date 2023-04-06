import ctypes

clib = ctypes.CDLL("./clib.so")

short_way = False

if short_way:
    clib.display(b"John", 10)
else:
    display = clib.display
    display.argtypes = [ctypes.c_char_p, ctypes.c_int]
    display.restype = ctypes.c_char_p

    string = display(b"John", 10)
    print(string.decode("utf-8"))
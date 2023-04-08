import ctypes, os

if __name__ == "__main__":
    cwd_path = os.getcwd()
    lib_name = "clib.so"
    clib = ctypes.CDLL(os.path.join(cwd_path, lib_name))

    print_hello = clib.print_hello
    print_hello.argtypes = ()
    print_hello.restype = None

    print_hello()
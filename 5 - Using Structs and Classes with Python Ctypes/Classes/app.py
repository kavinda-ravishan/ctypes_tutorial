import ctypes, os

class Point_Imp(ctypes.Structure):
    _fields_ = (
        ("x", ctypes.c_int32), 
        ("y", ctypes.c_int32) 
    )

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Point:
    def __init__(self, x, y):
        self.__get_point_func = clib.get_point
        self.__get_point_func.argtypes = (ctypes.c_int32, ctypes.c_int32)
        self.__get_point_func.restype = ctypes.POINTER(Point_Imp)

        self.__free_point_func = clib.free_point
        self.__free_point_func.argtypes = (ctypes.POINTER(Point_Imp), )
        self.__free_point_func.restype = None

        self.__print_point_func = clib.print_point
        self.__print_point_func.argtypes = (ctypes.POINTER(Point_Imp), )
        self.__print_point_func.restype = None

        self.point_ptr = self.__get_point_func(x, y)

    def print_point(self):
        self.__print_point_func(self.point_ptr)

    def __del__(self):
        self.__free_point_func(self.point_ptr)


if __name__ == "__main__":
    cwd_path = os.getcwd()
    lib_name = "clib.so"
    clib = ctypes.CDLL(os.path.join(cwd_path, lib_name))

    point = Point(123, 321)
    point.print_point()
    del point
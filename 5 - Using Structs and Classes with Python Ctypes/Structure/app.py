import ctypes, os

class Point(ctypes.Structure):

    _fields_ = (
        ("x", ctypes.c_int32),
        ("y", ctypes.c_int32)
    )

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Points_Array(ctypes.Structure):
    _fields_ = (
        ("Points", Point * 2), 
    )


class Student(ctypes.Structure):

    _fields_ = (
        ("name", ctypes.c_char_p),
    )

    def __init__(self, name):
        self.name = name

if __name__ == "__main__":
    cwd_path = os.getcwd()
    lib_name = "clib.so"
    clib = ctypes.CDLL(os.path.join(cwd_path, lib_name))

    point = Point(1, 2)
    print(point)

    # example 1
    print_point_ptr = clib.print_point_ptr
    print_point_ptr.argtypes = (ctypes.POINTER(Point), )
    print_point_ptr.restype = None
    print_point_ptr(point)
    print_point_ptr(ctypes.pointer(point))

    print_point = clib.print_point
    print_point.argtypes = (Point, )
    print_point.restype = None
    print_point(point)

    # example 2
    get_point = clib.get_point
    get_point.argtypes = (ctypes.c_int32, ctypes.c_int32)
    get_point.restype = ctypes.POINTER(Point)

    free_point = clib.free_point
    free_point.argtypes = (ctypes.POINTER(Point), )
    free_point.restype = None

    point_ptr = get_point(12, 21)
    print(f"x : {point_ptr.contents.x}, y : {point_ptr.contents.y}")
    print_point_ptr(point_ptr)
    free_point(point_ptr)
    
    # example 3
    print_student_name = clib.print_student_name
    print_student_name.argtypes = (ctypes.POINTER(Student), )
    print_student_name.restype = None

    me = Student(b"John")
    print_student_name(ctypes.pointer(me))

    name = "Sam"
    friend = Student(bytes(name, 'utf-8'))
    print_student_name(ctypes.pointer(friend))

    # example 4
    points = (Point(1, 2), Point(3, 4))
    points_array = Points_Array(points)

    print_points_array = clib.print_points_array
    print_points_array.argtypes = (ctypes.POINTER(Points_Array), )
    print_points_array.restype = None

    print_points_array(points_array)
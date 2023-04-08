#pragma once

#include <cinttypes>
#include <cstdlib>
#include <cstdio>
#include <cstring>

struct Point
{
    int32_t x, y;

    Point(int32_t x, int32_t y);
};

struct Points_Array
{
    Point points[2];
};

struct Student
{
    char* name;
};

extern "C" void print_point(Point point);
extern "C" void print_point_ptr(Point* point_ptr);
extern "C" Point* get_point(int32_t x, int32_t y);
extern "C" void free_point(Point* point_ptr);
extern "C" void print_student_name(Student* student);
extern "C"  void print_points_array(Points_Array* points_array_ptr);
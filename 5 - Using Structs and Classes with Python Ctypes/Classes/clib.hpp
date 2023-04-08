#pragma once

#include <cinttypes>
#include <cstdlib>
#include <cstdio>
#include <cstring>

class Point
{
private:
    int32_t x, y;
public:
    Point(int32_t x, int32_t y);
    void print_point();
};

extern "C" void print_point(Point* point_ptr);
extern "C" Point* get_point(int32_t x, int32_t y);
extern "C" void free_point(Point* point_ptr);
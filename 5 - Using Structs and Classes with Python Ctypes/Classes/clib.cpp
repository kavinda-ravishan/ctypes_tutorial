#include "clib.hpp"

Point::Point(int32_t x, int32_t y): x(x), y(y){}

void Point::print_point()
{
    printf("x : %i, y : %i\n", x, y);
}

void print_point(Point* point_ptr)
{
    point_ptr->print_point();
}

Point* get_point(int32_t x, int32_t y)
{
    return new Point(x, y);
}

void free_point(Point* point_ptr)
{
    delete point_ptr;
}
#include "clib.hpp"

Point::Point(int32_t x, int32_t y): x(x), y(y){}

void print_point(Point point)
{
    printf("x : %i, y : %i\n", point.x, point.y);
}

void print_point_ptr(Point* point_ptr)
{
    printf("x : %i, y : %i\n", point_ptr->x, point_ptr->y);
}

Point* get_point(int32_t x, int32_t y)
{
    return new Point(x, y);
}
void free_point(Point* point_ptr)
{
    free(point_ptr);
}

void print_student_name(Student* student_ptr)
{
    printf("Name : %s\n", student_ptr->name);
}

void print_points_array(Points_Array* points_array_ptr)
{
    for(int i=0; i<2; i++)
    {
        printf("%i - x : %i, y : %i\n", i, points_array_ptr->points[i].x, points_array_ptr->points[i].y);
    }
}
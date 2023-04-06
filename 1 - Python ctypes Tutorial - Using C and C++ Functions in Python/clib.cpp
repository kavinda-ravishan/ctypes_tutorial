#include "clib.hpp"

const char* display(const char* name, int age)
{
    char* formatted_string = (char*)malloc(50);
    sprintf(formatted_string, "Name : %s, Age : %i", name, age);
    return formatted_string;
}
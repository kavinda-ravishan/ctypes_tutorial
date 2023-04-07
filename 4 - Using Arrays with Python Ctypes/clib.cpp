#include "clib.hpp"

void init_arr(int32_t* arr_ptr, const uint32_t arr_size)
{
    for(int i=0; i<arr_size; i++)
    {
        arr_ptr[i] = i;
    }
}

int32_t* get_array(const uint32_t arr_size)
{
    printf("Array Allocated\n");
    int32_t* arr_ptr = new int32_t[arr_size];

    for(int i=0; i<arr_size; i++)
    {
        arr_ptr[i] = i;
    }

    return arr_ptr;
}

void free_array(int32_t* arr_ptr)
{
    printf("Array freed\n");
    free(arr_ptr);
}
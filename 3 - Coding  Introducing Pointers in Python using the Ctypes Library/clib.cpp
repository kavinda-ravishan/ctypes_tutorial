#include "clib.hpp"

char* alloc_memory()
{
    char* str = strdup("hello from python");
    printf("Memory allocated\n");
    return str;
} 

void free_memory(char* addr)
{
    free(addr);
    printf("Memory freed\n");
}
#pragma once

#include <cinttypes>
#include <cstdlib>
#include <cstdio>
#include <cstring>

extern "C" void init_arr(int32_t* arr_ptr, const uint32_t arr_size);

extern "C" int32_t* get_array(const uint32_t arr_size);
extern "C" void free_array(int32_t* arr_ptr);
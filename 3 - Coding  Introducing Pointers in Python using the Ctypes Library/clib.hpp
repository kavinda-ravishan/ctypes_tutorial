#pragma once

#include <cstdlib>
#include <cstdio>
#include <cstring>

extern "C" char* alloc_memory();
extern "C" void free_memory(char* addr);
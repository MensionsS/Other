#include <stdio.h>
#include <stdarg.h>

int my_printf(const char* format) {
    va_list args;
    va_start(args, format);
    int count = vprintf(format, args);
    va_end(args);
    return count;
}
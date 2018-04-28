#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  if (argc > 1) {
    char* ptr = getenv(argv[1]);
    printf("%p\n", ptr);
  }
}

#include <stdio.h>

int main(void) {
  char a[4] = "jum";
  int* tmp = (int*)a;

  for (int i = 0; i <= 7; i++) {
    *tmp += 5;
  }

  printf("The address is 0x%08X\n", *tmp);

  return 0;
}

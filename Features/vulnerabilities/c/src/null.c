#include <stdio.h>
#include <string.h>

#define S 100
#define N 1000


int main(int argc, char *argv[]) {
  char out[S];
  char buf[N];
  char msg[] = "Enter an IP adress\n";
  int len = 0;
  int * pointer = NULL;
  int value = *pointer; /* Dereferencing happens here */

  buf[0] = value;
  printf(msg);
  while (argc) {
    sprintf(out, "argument %d is %s\n", argc-1, argv[argc-1]);
    argc--;
    strncat(buf,out,sizeof(buf)-len-1);
    len = strlen(buf);
  }
  printf("%s",buf);

  return 0;
}

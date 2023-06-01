#include <stdio.h>
#include <string.h>

#define S 100
#define N 1000
#include <map>
#include <numeric>
#include <iostream>

using namespace std;

map<string,string> parseArgs(int argc, char *argv[]){
    map<string,string> args; 
    for (int i = 1; i < argc-1; i += 2) {
        string name = string(argv[i]);
        name = name[0]=='-'? name.substr(1) : name;
        args[name] = string(argv[i+1]);
    }
    return args;
}

int main(int argc, char *argv[]) {
  map<string,string> args = parseArgs(argc, argv);

  auto key = args.find("M");
  if (key->second == "GET"){
      printf("Welcome the very usefull echoing program! \n");
      printf("Format: \"-d data\" \n");
  }else if (key->second == "POST"){
    char out[S];
    char buf[N];
    char msg[] = "Welcome to the argument echoing program\n";
    int len = 0;
    buf[0] = '\0';
    printf(msg);
    while (argc) {
      sprintf(out, "argument %d is %s\n", argc-1, argv[argc-1]);
      argc--;
      strncat(buf,out,sizeof(buf)-len-1);
      len = strlen(buf);
    }
    printf("%s",buf);
  }
    return 0;
}

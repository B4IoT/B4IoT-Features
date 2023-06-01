#include <stdlib.h>
#include <stdio.h>
#include <string.h>
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

int main(int argc, char **argv)
{   
    map<string,string> args = parseArgs(argc, argv);

    auto key = args.find("M");
    if (key->second == "GET"){
        printf("Enter a program that you want to get to known the time of! \n");
        printf("Format: \"-prog program_name\" \n");
    }else if (key->second == "POST"){
        //if(argc != 2) {
        //     printf("Error: Please enter a program to time!\n");
        //     return -1;
        //}
        auto test = args.find("prog");
        string command = "time ./" ;

        command.append(test->second);
        int n = command.length();
 
        // declaring character array
        char char_array[n + 1];
        strcpy(char_array, command.c_str());

        system(char_array);
    }
     return 0;
}
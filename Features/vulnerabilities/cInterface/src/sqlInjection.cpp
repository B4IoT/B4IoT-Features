#include <stdio.h>
#include <stdlib.h>
#include <sqlite3.h> 
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
static int callback(void *data, int argc, char **argv, char **azColName){
   int i;
   fprintf(stderr, "%s: ", (const char*)data);
   
   for(i = 0; i<argc; i++){
      printf("%s = %s\n", azColName[i], argv[i] ? argv[i] : "NULL");
   }
   
   printf("\n");
   return 0;
}

int main(int argc, char* argv[]) {
    map<string,string> args = parseArgs(argc, argv);

    auto key = args.find("M");
    if (key->second == "GET"){
        printf("Enter your username and password to get your personal data! \n");
        printf("Format: \"-u username -p password\" \n");
    }else if (key->second == "POST"){
    sqlite3 *db;
    char *zErrMsg = 0;
    int rc;
    //char *sql;
    const char* data = "Callback function called";
        rc = sqlite3_open("login.db", &db);

        if( rc ) {
            fprintf(stderr, "Can't open database: %s\n", sqlite3_errmsg(db));
            return(0);
        } else {
            fprintf(stderr, "Opened database successfully\n");
        }
        /* Create SQL statement */

        string email = args.find("u")->second;
       
        int n = email.length();
        // declaring character array
        char char_email[n + 1];
        strcpy(char_email, email.c_str());

        string password = args.find("p")->second;
        
        n = password.length();
        // declaring character array
        char char_pass[n + 1];
        strcpy(char_pass, password.c_str());


        char sql[100] = "SELECT * FROM login where email = '";
        strncat(sql, char_email, 50);
        strncat(sql, "' and password = '",19 );
        strncat(sql, char_pass, 10);
        strncat(sql, "'", 2);




        fprintf(stderr,"your statement is: %s ",sql);

        /* Execute SQL statement */
        rc = sqlite3_exec(db, sql, callback, (void*)data, &zErrMsg);

        if( rc != SQLITE_OK ) {
            fprintf(stderr, "SQL error: %s\n", zErrMsg);
            sqlite3_free(zErrMsg);
        } else {
            fprintf(stdout, "Operation done successfully\n");
        }

        sqlite3_close(db);
    }
}

#include <stdio.h>
#include <stdlib.h>
#include <sqlite3.h> 
#include <cstring>

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
    char email[15];
    fprintf(stderr, "Enter your email: ");
    fgets(email,50,stdin);
    email[strcspn(email, "\n")] = 0;

    fprintf(stderr,"you entered: %s ",email);

    char password[15];
    fprintf(stderr,"Enter your password: ");
    fgets(password,50,stdin);
    password[strcspn(password, "\n")] = 0;
    fprintf(stderr,"you entered: %s ",password);

    char sql[100] = "SELECT * FROM login where email = '";
    strncat(sql, email, 15);
    strncat(sql, "' and password = '",19 );
    strncat(sql, password, 10);
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

package SQL_Injection;

import java.sql.*;
import java.util.HashMap;
import java.util.Objects;
import java.util.Scanner;

public class SqlInjection {
    public static void main( String argsv[] ) {
        HashMap<String, String> args = new HashMap<>();

        for (int i = 0; i < argsv.length; i=i+2){
            String name = argsv[i].substring(1);
            args.put(name, argsv[i+1]);
        }
        if (Objects.equals(args.get("M"), "GET")){
            System.out.println("Enter your email and password to authenticate");
            System.out.println("Format: \"-user username -pass password\"");
        }else if(Objects.equals(args.get("M"), "POST")) {
            Connection c = null;
            Statement stmt = null;

            try {
                Class.forName("org.sqlite.JDBC");
                c = DriverManager.getConnection("jdbc:sqlite:./login.db");
                c.setAutoCommit(false);
                System.out.println("Opened database successfully");

                stmt = c.createStatement();
                String email = args.get("user");

                String password = args.get("pass");
                String sqlString = "SELECT * FROM login WHERE email = \'" + email + "\' and password = \'" + password + "\'";
                ResultSet rs = stmt.executeQuery(sqlString);

                while (rs.next()) {
                    int id = rs.getInt("id");
                    String email2 = rs.getString("email");
                    String password2 = rs.getString("password");

                    System.out.println("ID = " + id);
                    System.out.println("NAME = " + email2);
                    System.out.println("AGE = " + password2);
                    System.out.println();
                }
                rs.close();
                stmt.close();
                c.close();

            } catch (Exception e) {
                System.err.println(e.getClass().getName() + ": " + e.getMessage());
                System.exit(0);
            }
            System.out.println("Opened database successfully");
        }
        }
}

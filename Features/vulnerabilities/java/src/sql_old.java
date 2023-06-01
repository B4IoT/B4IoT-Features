package SQL_Injection;

import java.sql.*;
import java.util.Scanner;

public class sql_old {
    public static void main( String args[] ) {
        Connection c = null;
        Statement stmt = null;

        try {
            Class.forName("org.sqlite.JDBC");
            c = DriverManager.getConnection("jdbc:sqlite:./login.db");
            c.setAutoCommit(false);
            System.out.println("Opened database successfully");

            stmt = c.createStatement();
            System.out.println("Please enter your email: ");
            Scanner sc=new Scanner(System.in);
            String email = sc.nextLine();

            System.out.println("Please enter your password: ");
            String password = sc.nextLine();
            String sqlString = "SELECT * FROM login WHERE email = \'" +email + "\' and password = \'"+ password +"\'" ;
            ResultSet rs = stmt.executeQuery( sqlString );

            while ( rs.next() ) {
                int id = rs.getInt("id");
                String  email2 = rs.getString("email");
                String  password2 = rs.getString("password");

                System.out.println( "ID = " + id );
                System.out.println( "NAME = " + email2 );
                System.out.println( "AGE = " + password2 );
                System.out.println();
            }
            rs.close();
            stmt.close();
            c.close();

        } catch ( Exception e ) {
            System.err.println( e.getClass().getName() + ": " + e.getMessage() );
            System.exit(0);
        }
        System.out.println("Opened database successfully");
    }
}
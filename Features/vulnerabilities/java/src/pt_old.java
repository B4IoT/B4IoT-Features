import java.io.File;
import java.util.Scanner;

class PathTraversal {
    public static void main(String[] args) {
        System.out.println("Hello Vulnerable World!"); // Display the string.
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter Path");
        String path = sc.nextLine();

        if (path.startsWith("/home/client/"))
        {
            File f = new File(path);
            f.delete();
        }
    }
}
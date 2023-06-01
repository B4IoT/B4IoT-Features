import java.io.File;
import java.util.HashMap;
import java.util.Objects;
import java.util.Scanner;

class PathTraversal {
    public static void main(String[] argsv) {
        HashMap<String, String> args = new HashMap<>();

        for (int i = 0; i < argsv.length; i = i + 2) {
            String name = argsv[i].substring(1);
            args.put(name, argsv[i + 1]);
        }
        if (Objects.equals(args.get("M"), "GET")) {
            System.out.println("Enter the file in your home folder you want to delete in your home folder!");
            System.out.println("Format: \"-p path\"");
        } else if (Objects.equals(args.get("M"), "POST")) {

            System.out.println("Hello Vulnerable World!"); // Display the string.
            String path = args.get("p");

            if (path.startsWith("/home/client/")) {
                File f = new File(path);
                f.delete();
            }
        }
    }
}

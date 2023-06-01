import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Objects;

public class CI_old{


    public static void main(String[] argsv){

            String user = args.get("user");
            String user_path = "/home/"+user;
            File file = new File(user_path);

            try {
                String comm = "ls "+user_path ;
                System.out.println("Your command will be: "+ comm);
                Process process = Runtime.getRuntime().exec(comm);

                StringBuilder output = new StringBuilder();

                BufferedReader reader = new BufferedReader(
                        new InputStreamReader(process.getInputStream()));

                String line;
                while ((line = reader.readLine()) != null) {
                    output.append(line + "\n");
                }

                int exitVal = process.waitFor();
                if (exitVal == 0) {
                    System.out.println("Success!");
                    System.out.println(output);
                } else {
                    System.out.println(output);
                }
            }
            catch (IOException | InterruptedException e) {
                System.out.println("Error executing command");
            }
            System.out.println("Done");
        }

    }
}
import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Objects;

public class commandInjection{


    public static void main(String[] argsv){
        HashMap<String, String> args = new HashMap<>();

        for (int i = 0; i < argsv.length; i=i+2){
            String name = argsv[i].substring(1);
            args.put(name, argsv[i+1]);
        }
        if (Objects.equals(args.get("M"), "GET")){
            System.out.println("Enter your username to see the content of your home directory");
            System.out.println("Format: \"-user username\"");
        }else if(Objects.equals(args.get("M"), "POST")){

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
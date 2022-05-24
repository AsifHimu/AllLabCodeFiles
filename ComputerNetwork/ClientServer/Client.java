import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.net.Socket;
import java.util.Scanner;

public class Client {
    public static void main(String[] args)throws Exception {
        System.out.println("Client started...");
        Socket socket = new Socket("127.0.0.1",12345);
        System.out.println("Client connected.");

        while(true){
            System.out.println("Enter the message...");

            DataInputStream in = new DataInputStream(socket.getInputStream());
            DataOutputStream out = new DataOutputStream(socket.getOutputStream());

            Scanner scanner = new Scanner(System.in);
            String input = scanner.nextLine();

            out.writeUTF(input);

            String response = in.readUTF();
            System.out.println(response); 
        }
    }
}
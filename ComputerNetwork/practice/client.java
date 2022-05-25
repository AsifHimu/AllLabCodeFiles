import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.net.Socket;
import java.util.Scanner;

public class client {
    public static void main(String[] args)throws Exception {
        System.out.println("Client started..");
        Socket socket = new Socket("127.0.0.1", 12345);
        System.out.println("Client connected");

        DataInputStream in = new DataInputStream(socket.getInputStream());
        DataOutputStream out = new DataOutputStream(socket.getOutputStream());

        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();

        out.writeUTF(input);
        String response = in.readUTF();
        System.out.println(response);
    }
}

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class server {
    public static void main(String[] args)throws Exception {
        ServerSocket serverSocket = new ServerSocket(12345);
        System.out.println("Server started..");
        Socket socket = serverSocket.accept();
        System.out.println("Client connected.");

        System.out.println("Waiting for input");

        DataInputStream in = new DataInputStream(socket.getInputStream());
        DataOutputStream out = new DataOutputStream(socket.getOutputStream());

        String msg = in.readUTF();

        System.out.println(msg);
        msg = "Response from server :"+msg+"("+new java.util.Date()+")";
        out.writeUTF(msg);
    }
}
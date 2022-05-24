import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {
    public static void main(String[] args)throws Exception {
        ServerSocket serverSocket = new ServerSocket(12345);
        System.out.println("Server started...");
        Socket socket = serverSocket.accept();
        System.out.println("Client connected");

        System.out.println("Waiting for input..");
        while(true){
            DataInputStream in = new DataInputStream(socket.getInputStream());
            DataOutputStream out = new DataOutputStream(socket.getOutputStream());

            String msg = in.readUTF();

            if(msg.equalsIgnoreCase("exit")){
                System.out.println("Exiting....");
                break;
            }

            System.out.println(msg);

            msg = "Response from server :"+"welcome"+"(" +new java.util.Date()+")";
            out.writeUTF(msg);
        }
    }
}

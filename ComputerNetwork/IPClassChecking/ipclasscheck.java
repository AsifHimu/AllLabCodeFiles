import java.util.Scanner;

public class ipclasscheck {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the IP address: ");
        String iip = "";
        String ip = sc.nextLine();
        int dot=0;
        for(int i=0;i<ip.length();i++){
            if(ip.charAt(i) == '.'){
                dot++;
            }
            if(dot<1){
                iip += ip.charAt(i);
            }
        }
        if(dot != 3){
            System.out.println("Invalid IP Address");
            System.exit(0);
        }
        int val = Integer.parseInt(iip);
        String iiip = Integer.toBinaryString(val);

        int lengthB = iiip.length();
        int missingZero = 8 - lengthB;
        iiip = "0".repeat(missingZero) + iiip;

       // System.out.println(iiip);

        if(iiip.charAt(0) == '0'){
            System.out.println("Class A");
            System.exit(0);
        }
        if (iiip.charAt(1) == '0') {
            System.out.println("Class B");
            System.exit(0);
        }
        if (iiip.charAt(2) == '0') {
            System.out.println("Class C");
            System.exit(0);
        }
        if (iiip.charAt(3) == '0') {
            System.out.println("Class D");
            System.exit(0);
        }
        if (iiip.charAt(3) == '1') {
            System.out.println("Class E");
            System.exit(0);
        }
    }
}

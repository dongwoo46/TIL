package Basic;

import java.util.Scanner;

public class Multiply {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        int B = sc.nextInt();
        

        System.out.println(A * B);

        sc.close();
    }
}

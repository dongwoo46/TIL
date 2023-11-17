package Basic;

import java.util.Scanner;

public class Java10430 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();

        int first = (A + B) % C;
        int second = ((A % C) + (B % C)) % C;
        int third = (A*B)%C;
        int fourth = ((A % C) * (B % C)) % C;

        System.out.println(first);
        System.out.println(second);
        System.out.println(third);
        System.out.println(fourth);
    }
}

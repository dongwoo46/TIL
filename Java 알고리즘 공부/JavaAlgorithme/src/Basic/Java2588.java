package Basic;

import java.util.Scanner;

public class Java2588 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        String A = sc.next();
        String B = sc.next();

        int first = Integer.parseInt(String.valueOf(B.charAt(2))) * Integer.parseInt(String.valueOf(A));
        int second = Integer.parseInt(String.valueOf(B.charAt(1))) * Integer.parseInt(String.valueOf(A));
        int third = Integer.parseInt(String.valueOf(B.charAt(0))) * Integer.parseInt(String.valueOf(A));
        int fourth = Integer.parseInt(String.valueOf(B)) * Integer.parseInt(String.valueOf(A));

        System.out.println(first);
        System.out.println(second);
        System.out.println(third);
        System.out.println(fourth);

    }
}

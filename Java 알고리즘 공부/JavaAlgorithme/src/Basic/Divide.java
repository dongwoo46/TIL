package Basic;

import java.util.Scanner;

public class Divide {

    public static void main(String[] args) throws Exception {

        Scanner sc = new Scanner(System.in);

        double A = sc.nextDouble(); // 수정된 부분
        double B = sc.nextDouble();

        System.out.println(A/B);
        sc.close();
    }
}

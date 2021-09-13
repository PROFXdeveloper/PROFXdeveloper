// how to create Simple calculator in Java

// thats all bye 
import java.util.*;

public class Calculator{
    public static void main(String[]args){
        Scanner scan = new Scanner(System.in);

        System.out.print("Enter num1: ");
        int num1 = scan.nextInt();
        System.out.print("Enter num2: ");
        int num2 = scan.nextInt();
        System.out.print("Select operation to perform(+ * - /) : ");
        String operator = scan.next();


        scan.close();

        switch(operator){

            case "+":
            System.out.print(num1+num2);
            break;
            case "-":
            System.out.print(num1-num2);
            break;
            case "*":
            System.out.print(num1*num2);
            break;
            case "/":
            System.out.print(num1/num2);
            break;
        }

    }
}
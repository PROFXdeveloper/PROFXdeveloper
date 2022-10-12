import java.util.*;


public class Calculator {
    public static void main(String[]args){


        Scanner scan = new Scanner(System.in);
        String repeat;
    do{

    
        System.out.println("Select operation to perform ");

        String[] names = {"1. Add ","2. Subtraction ", "3. Mult." };

        for(int i = 0; i< names.length; i++){

            System.out.println(names[i]);

        }
        System.out.println("");
        int operation = scan.nextInt();

        System.out.println("enter a no. ");
        int num1 = scan.nextInt();

        System.out.println("enter a no. ");
        int num2 = scan.nextInt();

        
    

        if (operation == 1){
            System.out.print("Answer ");
            System.out.println(num1 + num2);
        }
        else if (operation == 2){
            System.out.print("Answer ");
            System.out.println(num1-num2);

        }
        else if (operation == 3){
            System.out.print("Answer ");
            System.out.println(num1*num2);

        }
      
        System.out.println("Repeat the operation y or n");
        repeat= scan.next();

       }

       while (repeat.equalsIgnoreCase("y"));
       
    }

}


import java.util.*;

public class App {
    public static void main(String[] args)  {
     String answer;
     Scanner scan = new Scanner(System.in);
    do{
       System.out.println("_____________PROFX CALCULATOR_______________");
       System.out.println("SELECT OPERATION TO PERFORM");
       System.out.println("1-ADDITION");
       System.out.println("2-SUBTRACTION");
       System.out.println("3-MULTIPLICATION");
       System.out.println("4-DIVISION");
       int operator = scan.nextInt();

       System.out.println("ENTER FIRST #");
       int x = scan.nextInt();
       System.out.println("ENTER SECOND #");
       int y = scan.nextInt();

      
       
       if(operator == 1){
        System.out.println("Answer = " + add(x, y));
       }
       else if(operator == 2){
        System.out.println("Answer = " + sub(x, y));
       }
       else if(operator == 3){
        System.out.println("Answer = " + mul(x, y));
       }
       else if(operator == 4){
        System.out.println("Answer = " + div(x, y));
       }
       
       
       System.out.println("Repeat operation y or n ?");
       answer = scan.next();
    }

    
    while (answer.equalsIgnoreCase("y")); 

    
    do{
    System.out.print("Goodbye");
    }       
    while (answer.equalsIgnoreCase("n")); 
    

    }
     public static int add( int x,int y){
       int n;
       n = x+y;
       return n;


    }
    public static int sub( int x,int y){
        int n;
        n = x-y;
        return n;
 
 
    }
    public static int mul( int x,int y){
        int n;
        n = x*y;
        return n;
 
 
     }
     public static int div( int x,int y){
        int n;
        n = x/y;
        return n;
 
 
     }
     
     
     
    
}

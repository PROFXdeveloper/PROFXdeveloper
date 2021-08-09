import java.util.Scanner;
public class Main
{
	public static void main(String[] args)
	{
	   Scanner s =new Scanner(System.in);
		
		int row;
		int colums;
		String symbol ;
		
		System.out.print("enter a number of row: ");
		row = s.nextInt();
		s.nextLine();
		
		System.out.print("enter a number of colums: ");
		colums= s.nextInt();
		s.nextLine();
		
		System.out.print("enter a symbol: ");
		symbol= s.nextLine();
		
		for (int i = 0; i<row; i++){
			System.out.println();
		for(int j = 0; j<colums; j++){
			System.out.print(symbol+" ");
			
			
			
		}
	  }
		
	}
		
		
}

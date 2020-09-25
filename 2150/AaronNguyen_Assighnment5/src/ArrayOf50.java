import java.util.Scanner;

public class ArrayOf50 {

	public static void main(String[] args) {
		
		Scanner input = new Scanner(System.in);
		int[] ListOf50 = new int[50];
		int i;
		//giving numbers to the array
		for(i = 0; i < 50; i++) {
			ListOf50[i] = (int)(Math.random() * 99);
		}
		//making it a 5 x 10 table
		for(i = 0; i < 50; i++) {
			
			if(i == 10 || i == 20 || i == 30 || i == 40 || i == 50) {
				System.out.print("\n"+ListOf50[i] + " ");
			}else {
				System.out.print(ListOf50[i] + " ");
			}
			
		}
		
			System.out.println("\nEnter an Index: ");
				int x = input.nextInt();
				
					while(x >= 0) {
						if(x >= 50) {
							CHECKING(x);	
						}else {
							System.out.println(ListOf50[x]);
						}
				
				
				x = input.nextInt();
				
				}	

	}
		//Checking if the input is a valid number
		public static void Checking(int x)throws IndexOutOfBoundsException {
			
			if(x >= 50) {
				throw new IndexOutOfBoundsException("Out of Bounds ");
			
			}
		}
		
		public static void CHECKING(int x) {
			
			try {
				Checking(x);
			}
			
			catch(IndexOutOfBoundsException e) {
			System.out.print( e.getMessage() + "Try Again ");
			
			}
		}
	

}

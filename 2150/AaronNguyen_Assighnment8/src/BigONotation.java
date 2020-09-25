import java.util.Scanner;

public class BigONotation {

	public static void main(String[] args) {
		
		Scanner input = new Scanner(System.in);
		
		int total = 0;
		System.out.print("Enter n1: ");
		int n1 = input.nextInt();
		
		System.out.print("Enter n2: ");
		int n2 = input.nextInt();
		
		for(int i = n1; i <= n2; i++) {
			total += i;
		}
		
		System.out.println(total);
//^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ should be O(n)
//below is O(1) 
//try finding way to do it in one step
//the sum of the first 100 == 5050 includes i <= n2
		//this part should be find
		
		total = n2*(n2 + 1)/2;
		System.out.println(total);
		
	}

}

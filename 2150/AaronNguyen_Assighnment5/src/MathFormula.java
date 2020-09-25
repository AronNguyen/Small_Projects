import java.util.InputMismatchException;
import java.util.Scanner;

public class MathFormula {

	public static void main(String[] args) {
		
		System.out.println("Enter Equation with not spaces");
		System.out.println("Example: 1+1");
		Scanner input = new Scanner(System.in);

		String x = "";
		
		while(x != "0") {
			x = input.nextLine();
			
			
			if(x.contains("+")) {
				
				System.out.println(Addition(x));
				
			}else if(x.contains("-")) {
				
				System.out.println(Subtraction(x));
				
			}else if(x.contains("/")) {
				
				System.out.println(Division(x));
				
			}else if(x.contains("*")) {
				
				System.out.println(Multiplication(x));
				
			}else {
				System.out.println("Invalid Operator. Try Again ");
			}
		}
		
	}
	
	public static void checking(String x) {
		try {
			checkingP2(x);
		}
		
		catch(InputMismatchException e) {
			System.out.println(e.getMessage() + "Try again ");
		}
	}
	
	public static void checkingP2(String x)throws InputMismatchException {
		int i;
		for(i = 0; i < x.length(); i++) {
			if(x.charAt(i) == '1') {
				
			}else if (x.charAt(i) == '2') {
				
			}else if (x.charAt(i) == '3') {
				
			}else if (x.charAt(i) == '4') {
				
			}else if (x.charAt(i) == '5') {
				
			}else if (x.charAt(i) == '6') {
				
			}else if (x.charAt(i) == '7') {
				
			}else if (x.charAt(i) == '8') {
				
			}else if (x.charAt(i) == '9') {
				
			}else if (x.charAt(i) == '0') {
				
			}else if (x.charAt(i) == '.') {
				
			}else {
				throw new InputMismatchException("Invalid number ");
			
		}
		}
		
	}
	
	
	public static double Conversion(String x) {
		
		double i = Double.parseDouble(x);
		
		return i;
	}
	
	public static double Addition(String x) {
		checking(x.substring(0, x.indexOf("+")));
		checking(x.substring(x.indexOf("+")+ 1, x.length()));
		double i = Conversion(x.substring(0, x.indexOf("+")));
		double o = Conversion(x.substring(x.indexOf("+")+ 1, x.length()));
		return i+o;
		
	}
	
	public static double Subtraction(String x) {
		
		double i = Conversion(x.substring(0, x.indexOf("-")));
		double o = Conversion(x.substring(x.indexOf("-") + 1, x.length()));
		return i-o;
		
	}
	
	public static double Division(String x) {
		
		double i = Conversion(x.substring(0, x.indexOf("/")));
		double o = Conversion(x.substring(x.indexOf("/") + 1, x.length()));
		return i/o;
		
	}
	
	public static double Multiplication(String x) {
		
		double i = Conversion(x.substring(0, x.indexOf("*")));
		double o = Conversion(x.substring(x.indexOf("*") + 1, x.length()));
		return i*o;
		
	}
	
}

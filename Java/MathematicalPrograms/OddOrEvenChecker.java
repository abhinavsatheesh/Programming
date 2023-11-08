import java.util.Scanner;
public class OddOrEvenChecker {
	public static void main(String[] args) {
		 Scanner scan = new Scanner(System.in);	
		 System.out.println("Enter a number");
		 int numentered = scan.nextInt();
		 if (numentered > 0) {
			 System.out.println("Your number " + numentered + " is Positive");
		 }
		 else {
			 System.out.println("Your number " + numentered + " is Negative");
		 }
	}
}
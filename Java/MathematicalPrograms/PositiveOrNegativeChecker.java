//Program to check whether a number is Postitive or Negative
import java.util.Scanner;
public class PositiveOrNegativeChecker {
	public static void main(String[] args) {
		 Scanner myObj = new Scanner(System.in);
		 System.out.println("Enter a number");
		 int num = myObj.nextInt();
		 if (num > 0) {
			 System.out.println("Your number " + num + " is positive");
		 }
		 else {
			 System.out.println("Your number " + num + " is negative");
		 }
	}
}
		 
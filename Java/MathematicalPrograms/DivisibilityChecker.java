//Program to check whether a number is divisible by a number or not
import java.util.Scanner;
public class DivisibilityChecker {
	public static void main(String[] args) {
		 Scanner myObj = new Scanner(System.in);
		 System.out.println("Enter a number");
		 int num1 = myObj.nextInt();
		 System.out.println("Enter a number by which we should check if " + num1 + " is divisible");
		 int num2 = myObj.nextInt();
		 if (num1 % num2 == 0) {
			 System.out.println("Your number " + num1 + " is divisible by " + num2);
		 }
		 else {
			 System.out.println("Your number " + num1 + " is not divisible by " + num2);
		 }
	}
}
		
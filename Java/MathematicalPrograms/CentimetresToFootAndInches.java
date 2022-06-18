//Convert your height from centimetres to inches and feet
import java.util.Scanner;
public class CentimetresToFootAndInches {
	public static void main(String[] args) {
		 Scanner scan = new Scanner(System.in);
		 System.out.println("Enter your height");
		 int num = scan.nextInt();
		 float dividebyinch = 2.54f;
		 float dividebyfoot = 30.48f;
		 float heightininch = num/dividebyinch;
		 float heightinfoot = num/dividebyfoot;
		 System.out.println("Height in inches = " + heightininch + ". Height in feet = " + heightinfoot);	
	}
}
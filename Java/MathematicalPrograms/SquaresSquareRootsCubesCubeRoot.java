import java.util.Scanner;
import java.lang.Math;
public class SquaresAndCubes {
	public static void main(String[] args) {
     Scanner myObj = new Scanner(System.in);
	 System.out.println("Enter a number");
	 double numper1 = myObj.nextInt();
	 System.out.println("Enter another number");
	 double numper2 = myObj.nextInt();
	 System.out.println("Enter a number");
	 double numper3 = myObj.nextInt();
	 System.out.println("Enter a number");
	 double numper4 = myObj.nextInt();
	 double square1 = Math.pow(numper1, 2);
	 double squareroot2 = Math.sqrt(numper2);
	 double cube3 = Math.pow(numper3, 3);
	 double cuberoot = Math.cbrt(numper4);
	 System.out.println("The square of number " + numper1 + " is " + square1 + ". The square root of " + numper2 + " is " + squareroot2 + ". The cube of number " + numper3 + " is " + cube3 + ". The cube root of " + numper4 + " is " + cuberoot);
	}
}
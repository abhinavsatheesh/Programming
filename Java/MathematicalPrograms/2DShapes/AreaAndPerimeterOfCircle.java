import java.util.Scanner;
import static java.lang.Math.*;

public class AreaAndPerimeterOfCircle {
	public static void main(String[] args) {
		Scanner myObj = new Scanner(System.in);
		System.out.println("Enter the Radius");
		int radiusper = myObj.nextInt();
		double a = PI*radiusper*radiusper;
		double perimeter = 2*PI*radiusper;
		System.out.println("Area = " + a);
		System.out.println("Perimeter = " + perimeter);
	}
}
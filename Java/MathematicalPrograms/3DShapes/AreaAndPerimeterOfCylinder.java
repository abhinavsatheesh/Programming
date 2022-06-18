import java.util.Scanner;
import java.lang.Math;

public class AreaAndPerimeterOfCylinder {
	public static void main(String[] args) {
		Scanner myObj = new Scanner(System.in);
		System.out.println("Enter the Radius");
		int radius = myObj.nextInt();
		System.out.println("Enter the Height");
		int height = myObj.nextInt();
		double c = 2*Math.PI*radius;
		System.out.println("Perimeter of the Bottom Circle is " + c + " cm");
		double a = Math.PI*Math.pow(radius, 2);
		System.out.println("Area of the Bottom Circle is " + a + " sq.cm.");
		double tsa = 2*Math.PI*radius*(radius+height);
		double lsa = 2*Math.PI*radius*height;
		System.out.println("Total Surface Area of the Cylinder is " + tsa + " sq.cm.");
		System.out.println("Lateral Surface Area of the Cylinder is " + lsa + " sq.cm.");
	}
}
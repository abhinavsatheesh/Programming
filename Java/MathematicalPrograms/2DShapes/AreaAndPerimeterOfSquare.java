import java.util.Scanner;
import java.lang.Math;
public class AreaAndPerimeterOfSquare {
	public static void main(String[] args) {
		Scanner myObj = new Scanner(System.in);
		System.out.println("Enter the Side measure");
		int side = myObj.nextInt();
		double peri = 4*side;
		double area = Math.pow(side, 2);
		System.out.println("Area = " + area + " sq.cm.");
		System.out.println("Perimeter = " + peri + " cm.");
	}
}
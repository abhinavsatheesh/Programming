//Program to find Area and Perimeter of Rectangle
import java.util.Scanner;
public class AreaAndPerimeterOfRectangle {
	public static void main(String[] args) {
		Scanner myObj = new Scanner(System.in);
		System.out.println("Enter a Length measure");
		int length = myObj.nextInt();
		System.out.println("Enter a Breadth measure");
		int breadth = myObj.nextInt();
		int area = length*breadth;
		int perimeter = 2*(length+breadth);
		System.out.println("Perimter = " + perimeter + " cm");
		System.out.println("Area = " + area + " sq.cm.");
	}
}
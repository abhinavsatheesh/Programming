//Program to find Area of Triangle
import java.util.Scanner;
public class AreaAndPerimeterOfTriangle {
	public static void main(String[] args) {
		Scanner myObj = new Scanner(System.in);
		System.out.println("Enter the length of 1st Side");
		int side1 = myObj.nextInt();
		System.out.println("Enter the length of 2nd Side");
		int side2 = myObj.nextInt();
		System.out.println("Enter the length of 3rd Side");
		int side3 = myObj.nextInt();
		double peri = side1+side2+side3;
		System.out.println("Perimeter of the Triangle is " + peri + " cm");
		System.out.println("Enter the breadth");
		int breadth = myObj.nextInt();
		System.out.println("Enter the height");
		int height = myObj.nextInt();
		double area = (breadth*height)/2;
		System.out.println("Area of the Triangle is " + area);
	}
}
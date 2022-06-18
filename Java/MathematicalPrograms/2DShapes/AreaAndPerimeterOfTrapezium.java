import java.util.Scanner;
public class AreaAndPerimeterOfTrapezium {
	public static void main(String[] args) {
		Scanner myObj = new Scanner(System.in);
		System.out.println("Enter the length of 1st Side");
		int side1 = myObj.nextInt();
		System.out.println("Enter the length of 2nd Side");
		int side2 = myObj.nextInt();
		System.out.println("Enter the length of 3rd Side");
		int side3 = myObj.nextInt();
		System.out.println("Enter the length of 4th Side");
		int side4 = myObj.nextInt();
		double perimeter = side1+side2+side3+side4;
		System.out.println("Perimeter of the Trapezium is " + perimeter + " cm");
		System.out.println("Enter the length of Base 1");
		int base_1 = myObj.nextInt();
		System.out.println("Enter the length of Base 2");
		int base_2 = myObj.nextInt();
		System.out.println("Enter the height of Trapezium");
		int height = myObj.nextInt();
		double area = ((base_1 + base_2) / 2) * height;
		System.out.println("Area of the Trapezium is " + area + " sq.cm.");
	}
}
		
		
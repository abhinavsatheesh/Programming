import java.util.Scanner;
public class AreaAndPerimeterOfQuadrilateral {
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
		int perimeter = side1+side2+side3+side4;
		System.out.println("Perimeter of the Quadrilateral is " + perimeter);
		System.out.println("Enter the length of Diagonal");
		int diagonal = myObj.nextInt();
		System.out.println("Enter the 1st Altitude");
		int altitude1 = myObj.nextInt();
		System.out.println("Enter the 2nd Altitude");
		int altitude2 = myObj.nextInt();
		int dss = diagonal/2;
		int hss = altitude1+altitude2;
		int area = dss*hss;
		System.out.println("Area of the Quadrilateral is " + area);		
	}
}
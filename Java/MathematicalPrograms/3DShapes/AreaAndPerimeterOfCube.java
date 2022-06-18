import java.util.Scanner;
public class AreaAndPerimeterOfCube {
	public static void main(String[] args) {
		Scanner myObj = new Scanner(System.in);
		System.out.println("Enter the side of the cube");
		int side = myObj.nextInt();
		double tsa = 6*side*side;
		double lsa = 4*side*side;
		System.out.println("Total Surface Area of Cube is " + tsa);
		System.out.println("Lateral Surface Area of Cube is " + lsa);
	}
}
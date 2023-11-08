import java.util.Scanner;
public class AreaAndPerimeterOfRhombus {
	public static void main(String[] args) {
		Scanner myObj = new Scanner(System.in);
		System.out.println("Enter the length of Diagonal 1");
		int diagonal1 = myObj.nextInt();
		System.out.println("Enter the length of Diagonal 2");
		int diagonal2 = myObj.nextInt();
		double area = 0.5*diagonal1*diagonal2;
		System.out.println("Area of Rhombus is " + area + " sq.cm.");
		System.out.println("Enter the side of the Rhombus");
		int side = myObj.nextInt();
		double peri = 4*side;
		System.out.println("Perimeter of the Rhombus is " + peri);
	}
}
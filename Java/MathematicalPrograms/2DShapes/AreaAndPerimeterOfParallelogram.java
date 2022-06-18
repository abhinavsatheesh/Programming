import java.util.Scanner;
public class AreaAndPerimeterOfParallelogram {
	public static void main(String[] args) {
		Scanner myObj = new Scanner(System.in);
		System.out.println("Enter the length of the Parallelogram");
		int length = myObj.nextInt();
		System.out.println("Enter the breadth of the Parallelogram");
		int breadth = myObj.nextInt();
		double area = length*breadth;
		double perimeter = 2*(length+breadth);
		System.out.println("Area of the Parallelogram is " + area);
		System.out.println("Perimeter of the Parallelogram is " + perimeter);
	}
}
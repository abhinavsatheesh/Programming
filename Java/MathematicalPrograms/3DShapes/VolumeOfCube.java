import java.util.Scanner;
import java.lang.Math;
public class VolumeOfCube {
	public static void main(String[] args) {
		Scanner myObj = new Scanner(System.in);
		System.out.println("Do you wish to find the Volume of Cube by 2D Method or via Side Method? Please enter either 2D or Side");
		String answer = myObj.nextLine();
		if (answer.equals("2D")) {
			System.out.println("OK.");
			System.out.println("Enter the Base Area of the Cube");
			int ba = myObj.nextInt();
			System.out.println("Enter a Height measure");
			int height = myObj.nextInt();
			int volume = ba*height;
			System.out.println("Volume of the Cube is " + volume);
		}
		else if (answer.equals("Side")) {
			System.out.println("OK.");
			System.out.println("Enter the measure of the Side");
			double side = myObj.nextInt();
			double volume = Math.pow(side, 3);
			System.out.println("Volume of the Cube is " + volume);
		}
		else {
			System.exit(0);
		}
	}
}
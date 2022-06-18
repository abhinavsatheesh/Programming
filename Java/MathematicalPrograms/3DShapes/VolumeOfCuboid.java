import java.util.Scanner;
import java.lang.Math;
public class VolumeOfCuboid {
	public static void main(String[] args) {
		Scanner myObj = new Scanner(System.in);
		System.out.println("Do you wish to find the Volume of Cuboid by 2D Method or via 3D Method? Please enter either 2D or 3D");
		String answer = myObj.nextLine();
		if (answer.equals("2D")) {
		    System.out.println("OK.");
			System.out.println("Enter the Base Area of the Cuboid");
			int ba = myObj.nextInt();
			System.out.println("Enter a Height measure");
			int height = myObj.nextInt();
			int volume = ba*height;
			System.out.println("Volume of the Cuboid is " + volume);
		}
		else if (answer.equals("3D")) {
		    	System.out.println("OK.");
				System.out.println("Enter a Length measure");
				double length = myObj.nextInt();
				System.out.println("Enter a Breadth measure");
				double breadth = myObj.nextInt();
				System.out.println("Enter a Height measure");
				double height = myObj.nextInt();
				double volume = length*breadth*height;
				System.out.println("Volume of the Cuboid is " + volume);
		}
		else {
			System.exit(0);
		}
	}
}
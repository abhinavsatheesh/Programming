import java.util.Scanner;
public class AreaAndPerimeterOfCuboid {
	public static void main(String[] args) {
		Scanner myObj = new Scanner(System.in);
		System.out.println("Enter a Length measure");
		int length = myObj.nextInt();
		System.out.println("Enter a Breadth measure");
		int breadth = myObj.nextInt();
		System.out.println("Enter a Height measure");
		int height = myObj.nextInt();
		int lengthbreadth = length*breadth;
		int lengthheight = length*height;
		int breadthheight = breadth*height;
		int tsa = 2*(lengthbreadth+lengthheight+breadthheight);
		int p = 4*(length+breadth+height);
		int lsa = 2*height*(length+breadth);
		System.out.println("Perimeter of the Cuboid is " + p + " cm");
		System.out.println("Total Surface Area of the Cuboid is " + tsa + " sq.cm.");
		System.out.println("Lateral Surface Area of the Cuboid is " + lsa + " sq.cm.");
	}
}
//Convert given length in metres to centimetres
import java.util.Scanner;
public class MetresToCentimetres {
	public static void main(String[] args) {
		 Scanner myQbj = new Scanner(System.in);
		 System.out.println("Enter the length in metres");
		 int lengthinmetres = myQbj.nextInt();
		 int lengthincenti = lengthinmetres*100;
		 System.out.println("Length in Centimetres = " + lengthincenti + " cm");
	}
}	
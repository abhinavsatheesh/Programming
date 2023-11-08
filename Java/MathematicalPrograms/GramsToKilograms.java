// Convert grams to kilograms
import java.util.Scanner;
public class GramsToKilograms {
	public static void main(String[] args) {
		Scanner myObj = new Scanner(System.in);
		System.out.println("Enter the Measurement in Grams");
		float grammeasure = myObj.nextFloat();
		float kilogrammeasure = grammeasure/1000;
		System.out.println("Weight in kilograms = " + kilogrammeasure + " kg");
	}
}
		 
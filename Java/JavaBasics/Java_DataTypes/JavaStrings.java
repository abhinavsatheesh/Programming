package Java_DataTypes;

import java.util.Scanner;
public class JavaStrings {
	public static void main(String[] args) {
		try (Scanner myObj = new Scanner(System.in)) {
			System.out.println("Enter your name");
			String Name = myObj.nextLine();
			System.out.println("Enter the place where you were born");
			String Place = myObj.nextLine();
			System.out.println("Enter the date when you were born");
			String Date = myObj.nextLine();
			System.out.println("Hello, " + Name + ". You were born in " + Place + " on " + Date);
		}
	}
}
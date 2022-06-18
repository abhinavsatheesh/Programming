//write a program to accept your name, class, division, school and print them
import java.util.Scanner;
public class NameClassSchool {
	public static void main(String[] args) {
		 Scanner myObj = new Scanner(System.in);
		 System.out.println("Enter your name");
		 String name = myObj.nextLine();
		 System.out.println("Enter your class and division");
		 String classdiv = myObj.nextLine();
		 System.out.println("Enter your school");
		 String school = myObj.nextLine();
		 System.out.println("Your name is " + name);
		 System.out.println("Your class and division is " + classdiv);
		 System.out.println("Your school is " + school);
	}
}	 
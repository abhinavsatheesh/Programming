import java.util.Scanner;
public class WhenToRetire{
	 public static void main(String[] args) {
		 Scanner myObj = new Scanner(System.in);
		 Scanner scan = new Scanner(System.in);
		 System.out.println("Enter your Name");
		 String name = myObj.nextLine();
		 System.out.println("Enter your Age");
		 int age = scan.nextInt();
		 System.out.println("Enter your Profession");
		 String profession = myObj.nextLine();
		 System.out.println("Enter your Retiring Age");
		 int retiring_age = scan.nextInt();
		 int yearsleft = retiring_age - age;
		 System.out.println("Hello " + name + ". Your age is " + age + ". Your profession is " + profession + ". You will have to retire from " + profession + " in " + yearsleft + " years");
	 }
}	
	
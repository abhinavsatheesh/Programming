import java.util.Scanner;
public class JavaFunctions {
	static void completereturn(String name, String job) {
		System.out.println("Hello " + name + ". Your job is " + job);
	}
	public static void main(String[] args) {
		try (Scanner myObj = new Scanner(System.in)) {
			System.out.println("May I know your name?");
			String Name = myObj.nextLine();
			System.out.println("May I know your job?");
			String Job = myObj.nextLine();
			completereturn(Name, Job);
		}
	}
}
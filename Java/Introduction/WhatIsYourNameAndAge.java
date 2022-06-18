import java.util.Scanner;
public class WhatIsYourNameAndAge{
	 public static void main(String[] args) {
		 Scanner myObj = new Scanner(System.in);
		 System.out.println("Enter your Name");
		 String name = myObj.nextLine();
		 System.out.println("Enter your Age");
		 String age = myObj.nextLine();
		 System.out.println("Hello " + name + ". Your age is " + age);
	 }
}
		 
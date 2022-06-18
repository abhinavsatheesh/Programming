import java.util.Scanner;
public class PrimeNumber {
	public static void main(String[] args) {
		 Scanner myObj = new Scanner(System.in);
		 System.out.println("Enter a number between 2 and 10");
		 int number = myObj.nextInt();
		 if (number>10 || number<2) {
		  System.out.println("This is a number off limits. Retry again.");
		 }
	     else {
		  if (number%2 == 0 && number>2) {
		    System.out.println(number + " is not a Prime Number");
		  }  
		  else if (number%3 == 0 && number!=3) {
		    System.out.println(number + " is a Prime Number");
		  }	
		  else {
		    System.out.println(number + " is a Prime Number");
		  }
	    }
	}
}


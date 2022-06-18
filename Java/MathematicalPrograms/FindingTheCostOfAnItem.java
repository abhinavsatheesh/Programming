// Finding the total cost of the item if quantity and price is given
import java.util.Scanner;
public class FindingTheCostOfAnItem {
	public static void main(String[] args) {
		 Scanner myObj = new Scanner(System.in);
		 System.out.println("Enter the name of the Item");
		 String itemname = myObj.nextLine();
		 System.out.println("Enter the quantity of the Item. Enter in Kilograms");
		 int weight = myObj.nextInt();
		 System.out.println("Enter the base price of the Item");
		 int baseprice = myObj.nextInt();
		 int finalprice = baseprice*weight;
		 System.out.println("Total Price for the item " + itemname + " is Rs. " + finalprice);
	}
}

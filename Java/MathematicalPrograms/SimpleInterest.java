import java.util.Scanner;
class SimpleInterest {
    public static void main(String[] args) {
        Scanner myObj = new Scanner(System.in);
        System.out.println("Enter the Principal Amount");
        int principal = myObj.nextInt();
        System.out.println("Enter the Time in Years");
        int time = myObj.nextInt();
        System.out.println("Enter the Rate of Interest");
        int rateofinterest = myObj.nextInt();
        int simpleinterest = principal*time*rateofinterest;
        int amount = principal + simpleinterest;
        System.out.println("Simple Interest is " + simpleinterest + " Rupees. Total Amount is " + amount + " Rupees");
    }
}
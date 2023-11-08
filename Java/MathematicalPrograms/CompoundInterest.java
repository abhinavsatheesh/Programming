import java.util.Scanner;
import java.lang.Math;
class CompoundInterest {
    public static void main(String[] args) {
        Scanner myObj = new Scanner(System.in);    
        System.out.println("Enter the Principal Amount");
        double principal = myObj.nextInt();
        System.out.println("Enter the Rate of Interest");
        double rateofinterest = myObj.nextInt();
        System.out.println("Enter the Time in Years");
        double time = myObj.nextInt();
        double rateof100 = 1+(rateofinterest/100);
        double raisedto = Math.pow(rateof100, time);
        double amount = principal*raisedto;
        double ci = amount-principal;
        System.out.println("Final Amount is " + amount);
        System.out.println("Compound Interest is " + ci);
    }
}
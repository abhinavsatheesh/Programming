import java.util.Scanner;
class RuleOf72 {
    public static void main(String[] args) { {
        Scanner myObj = new Scanner(System.in);
        System.out.println("Enter the Principal Amount");
        double principal = myObj.nextInt();
        System.out.println("Enter the Rate of Interest");
        double rateofinterest = myObj.nextInt();
        System.out.println("Your Principal Amount ₹ " + principal + " will become ₹ " + 2*principal + " in " + 72/rateofinterest + " years");
    }
}
}
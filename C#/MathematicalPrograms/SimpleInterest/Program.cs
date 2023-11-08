using System;

namespace SimpleInterest
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the Principal amount");
            double principal = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Enter the Rate of Interest");
            double rate = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Enter the Time in Years");
            double time = Convert.ToDouble(Console.ReadLine());
            double simpleInterest = (principal * rate * time) / 100;
            double amount = principal+simpleInterest;
            Console.WriteLine("Simple Interest = Rs. " + simpleInterest);
            Console.WriteLine("Amount = Rs. " + amount);
        }
    }
}

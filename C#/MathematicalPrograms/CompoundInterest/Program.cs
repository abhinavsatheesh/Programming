using System;

namespace CompoundInterest
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the Principal Amount");
            double principal = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Enter the no. of years");
            double years = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Enter the rate of interest");
            double rate = Convert.ToDouble(Console.ReadLine());
            double amount = principal*(Math.Pow(1+rate/100, years));
            double ci = amount-principal;
            Console.WriteLine("Compound Interest is Rs. " + ci);
            Console.WriteLine("Amount is Rs. " + amount);
        }
    }
}

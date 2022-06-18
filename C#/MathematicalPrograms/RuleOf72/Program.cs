using System;

namespace RuleOf72
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the Principal Amount");
            double principal = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Enter the Rate oF Interest");
            double rate = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Your Principal Amount Rs. " + principal + " will become " + 2*principal + " in " + 72/rate + " years");
        }
    }
}

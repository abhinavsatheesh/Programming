using System;

namespace DivisibilityChecker
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter a number");
            int a = int.Parse(Console.ReadLine());
            Console.WriteLine("Enter a number by which we should check if " + a + " is divisible");
            int b = int.Parse(Console.ReadLine());
            if (a%b == 0) {
                Console.WriteLine("Your number " + a + " is divisible by " + b);
            }
            else {
                Console.WriteLine("Your number " + a + " is not divisible by " + b);

            }
        }
    }
}

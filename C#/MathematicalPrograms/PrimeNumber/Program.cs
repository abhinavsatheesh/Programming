using System;

namespace PrimeNumber
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter a Number between 2 and 10.");
            int num = Convert.ToInt32(Console.ReadLine());
            if (num > 10 || num < 2) {
                Console.WriteLine("This is a number off limits. Retry again");
            }
            else {
                if (num%2 == 0 && num > 2) {
                    Console.WriteLine(num + " is not a Prime Number");
                }
                else if (num%3 == 0 && num != 3) {
                    Console.WriteLine(num + " is a Prime Number");
                }
                else {
                    Console.WriteLine(num + " is a Prime Number");
                }
            }
        }
    }
}

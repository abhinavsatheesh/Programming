using System;

namespace OddOrEvenChecker
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter a Number");
            int num = Convert.ToInt32(Console.ReadLine());
            if (num%2 == 0) {
                Console.WriteLine("Your number " + num + " is even");
            }
            else {
                Console.WriteLine("Your number " + num + " is odd");
            }
        }
    }
}

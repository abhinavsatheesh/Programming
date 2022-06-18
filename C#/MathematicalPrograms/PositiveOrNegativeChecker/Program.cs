using System;

namespace PositiveOrNegativeChecker
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter a number");
            int num = Convert.ToInt32(Console.ReadLine());
            if (num > 0){
                Console.WriteLine("Your number " + num + " is positive");
            }
            else if (num < 0){
                Console.WriteLine("Your number " + num + " is negative");
            }
            else {
                Console.WriteLine("Your number " + num + " is neither Positive or Negative");
            }
        }
    }
}

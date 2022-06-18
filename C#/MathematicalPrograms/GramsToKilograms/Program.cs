using System;

namespace GramsToKilograms
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the Measurement in Grams");
            double grams = Convert.ToDouble(Console.ReadLine());
            double kilograms = grams / 1000;
            Console.WriteLine("Weight in Kilograms is " + kilograms + " kg");
        }
    }
}

using System;

namespace CentimetresToFootAndInches
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter your height");
            double height = int.Parse(Console.ReadLine());
            double inch = height/2.54;
            double foot = height/30.48;
            Console.WriteLine("Height in Inches = " + inch);
            Console.WriteLine("Height in Feet = " + foot);
        }
    }
}

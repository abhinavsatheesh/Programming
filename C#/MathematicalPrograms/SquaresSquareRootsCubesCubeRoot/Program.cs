using System;

namespace SquaresSquareRootsCubesCubeRoot
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter a number");
            double num1 = Convert.ToDouble(Console.ReadLine());
            double sq = Math.Pow(num1, 2);
            Console.WriteLine("Enter another number");
            double num2 = Convert.ToDouble(Console.ReadLine());
            double cu = Math.Pow(num1, 3);
            Console.WriteLine("Enter another number");
            double num3 = Convert.ToDouble(Console.ReadLine());
            double root = Math.Sqrt(num3);
            Console.WriteLine("Enter another number");
            double num4 = Convert.ToDouble(Console.ReadLine());  
            double curoot = Math.Ceiling(Math.Pow(num4, (double) 1 / 3));  
            Console.WriteLine("The Square of the Number " + num1 + " = " + sq);
            Console.WriteLine("The Cube of the Number " + num2 + " = " + cu);
            Console.WriteLine("The Square Root of the Number " + num3 + " = " + root);
            Console.WriteLine("The Cube Root of the Number " + num4 + " = " + curoot);
        }
    }
}

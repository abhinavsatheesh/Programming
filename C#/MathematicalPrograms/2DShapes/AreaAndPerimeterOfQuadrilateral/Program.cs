using System;

namespace AreaAndPerimeterOfQuadrilateral
{
    class Program 
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the length of 1st Side");
            double side1 = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Enter the length of 2nd Side");
            double side2 = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Enter the length of 3rd Side");
            double side3 = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Enter the length of 4th Side");
            double side4 = Convert.ToDouble(Console.ReadLine());
            double perimeter = side1 + side2 + side3 + side4;
            Console.WriteLine("Perimeter of the Quadrilateral is " + perimeter);
            Console.WriteLine("Enter the Length of Diagonal");
            double d = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Enter the 1st Altitude");
            double h1 = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Enter the 2nd Altitude");
            double h2 = Convert.ToDouble(Console.ReadLine());
            double area = (d/2) * (h1+h2);
            Console.WriteLine("Area of the Quadrilateral is " + area);
        }
    }
}
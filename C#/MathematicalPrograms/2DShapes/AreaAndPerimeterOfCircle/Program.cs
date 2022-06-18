using System;

namespace AreaAndPerimeterOfCircle
{
    class Program
    {
        static void Main(string[] args)
        {
            double pi = Math.PI;
            Console.WriteLine("Enter the Radius");
            double radius = Convert.ToDouble(Console.ReadLine());
            double area = pi * radius * radius;
            double c = 2*pi*radius;
            Console.WriteLine("Area = " + area);
            Console.WriteLine("Perimeter = " + c);
        }
    }
}

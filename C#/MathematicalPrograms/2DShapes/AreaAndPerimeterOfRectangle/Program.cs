using System;

namespace AreaAndPerimeterOfRectangle
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the Length Measure");
            double Length = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Enter the Breadth Measure");
            double Breadth = Convert.ToDouble(Console.ReadLine());
            double area = Length * Breadth;
            double perimeter = 2 * (Length + Breadth);
            Console.WriteLine("Area = " + area);
            Console.WriteLine("Perimeter = " + perimeter);
        }
    }
}

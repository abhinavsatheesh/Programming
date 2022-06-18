using System;

namespace AreaAndPerimeterOfParallelogram
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the Length Measure");
            double Length = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Enter the Breadth Measure");
            double Breadth = Convert.ToDouble(Console.ReadLine());
            double area = Length*Breadth;
            double perimeter = 2*(Length+Breadth);
            Console.WriteLine("Area of the Parallelogram is " + area);
            Console.WriteLine("Perimeter of the Parallelogram is " + perimeter);
        }
    }
}

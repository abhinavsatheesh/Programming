using System;

namespace AreaAndPerimeterOfSquare
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the Side Measure");
            double s = Convert.ToDouble(Console.ReadLine());
            double area = s*s;
            double perimeter = 4*s;
            Console.WriteLine("Area = " + area + " sq.cm");
            Console.WriteLine("Perimeter = " + perimeter + " cm");
        }
    }
}

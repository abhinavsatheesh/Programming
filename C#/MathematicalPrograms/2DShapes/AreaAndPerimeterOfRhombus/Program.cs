using System;

namespace AreaAndPerimeterOfRhombus
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the Length of Diagonal 1");
            double d1 = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Enter the Length of Diagonal 2");
            double d2 = Convert.ToDouble(Console.ReadLine());
            double area = (d1*d2)/2;
            Console.WriteLine("Area of Rhombus is " + area + " sq.cm");
            Console.WriteLine("Enter the Side of the Rhombus");
            double side = Convert.ToDouble(Console.ReadLine());
            double perimeter = 4*side;
            Console.WriteLine("Perimeter of the Rhombus is " + perimeter + " cm");
        }
    }
}

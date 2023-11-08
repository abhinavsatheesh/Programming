using System;

namespace AreaAndPerimeterOfTrapezium
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
            double perimeter = side1+side2+side3+side4;
            Console.WriteLine("Perimeter of the Trapezium is " + perimeter + " cm");
            Console.WriteLine("Enter the Length of Base 1");
            double base1 = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Enter the Length of Base 2");
            double base2 = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Enter the Height of the Trapezium");
            double height = Convert.ToDouble(Console.ReadLine());
            double area = (base1+base2)*height/2;
            Console.WriteLine("Area of the Trapzium is " + area + " sq.cm");
        }
    }
}

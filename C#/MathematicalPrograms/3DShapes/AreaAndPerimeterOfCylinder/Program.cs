using System;

namespace AreaAndPerimeterOfCylinder 
{
    class Program 
    {
        static void Main(String[] args) {
            double pi = Math.PI;
            Console.WriteLine("Enter the Radius");
            double radius = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Enter the Height");
            double height = Convert.ToDouble(Console.ReadLine());
            double c = 2*pi*radius;
            double area = pi*radius*radius;
            double tsa = 2*pi*radius*(radius+height);
            double lsa = 2*pi*radius*height;
            Console.WriteLine("Perimeter of the Bottom Circle is " + c + " cm");
            Console.WriteLine("Area of the Bottom Circle is " + area + " sq.cm");
            Console.WriteLine("Total Surface Area of the Cylinder is " + tsa + " sq.cm");
            Console.WriteLine("Lateral Surface Area of the Cylinder is " + lsa + " sq.cm");
        }
    }
}
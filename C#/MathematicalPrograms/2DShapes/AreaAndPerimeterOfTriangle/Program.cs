using System;

namespace AreaAndPerimeterOfTriangle 
{
    class Program 
    {
        static void Main(String[] args) {
            Console.WriteLine("Enter the length of 1st Side");
            double side1 = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Enter the Length of 2nd Side");
            double side2 = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Enter the Length of 3rd Side");
            double side3 = Convert.ToDouble(Console.ReadLine());
            double perimeter = side1+side2+side3;
            Console.WriteLine("Perimeter of the Triangle is " + perimeter + " cm ");
            Console.WriteLine("Enter the Breadth");
            double breadth = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Enter the Height");
            double height = Convert.ToDouble(Console.ReadLine());
            double area = (breadth*height)/2;
            Console.WriteLine("Area of the Triangle is " + area);
        }
    }
}

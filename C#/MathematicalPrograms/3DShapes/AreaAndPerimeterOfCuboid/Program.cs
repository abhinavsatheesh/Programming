using System;

namespace AreaAndPerimeterOfCuboid 
{
    class Program 
    {
        static void Main(String[] args) {
            Console.WriteLine("Enter a Length Measure");
            double Length = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Enter a Breadth Measure");
            double breadth = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Enter a Height Measure");
            double height = Convert.ToDouble(Console.ReadLine());
            double tsa = 2*(Length*breadth + Length*height + breadth*height);
            double lsa = 2*height*(Length + breadth);
            double perimeter = 4*(Length+breadth+height);
            Console.WriteLine("Perimeter of the Cuboid is " + perimeter + " cm");
            Console.WriteLine("Total Surface Area of the Cuboid is " + tsa + " sq.cm");
            Console.WriteLine("Lateral Surface Area of the Cuboid is " + lsa + " sq.cm");
        }
    }
}
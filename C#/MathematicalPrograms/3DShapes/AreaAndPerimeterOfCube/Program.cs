using System;

namespace AreaAndPerimeterOfCube
{
    class Program 
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the Side of the Cube");
            double side = Convert.ToDouble(Console.ReadLine());
            double tsa = 6*side*side;
            double lsa = 4*side*side;
            Console.WriteLine("Total Surface Area of the Cube is " + tsa);
            Console.WriteLine("Lateral Surface Area of the Cube is " + lsa);
        }
    }
}

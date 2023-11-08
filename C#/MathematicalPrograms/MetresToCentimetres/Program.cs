using System;

namespace MetresToCentimetres
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the length in Metres");
            double metres = Convert.ToDouble(Console.ReadLine());
            double cm = metres*100;
            Console.WriteLine("Length in Centimetres = " + cm + " cm");
        }
    }
}

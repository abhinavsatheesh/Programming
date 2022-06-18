using System;

namespace VolumeOfCube
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Do you wish to find the Volume of Cube by 2D Method or via Side Method? Please enter either 2D or Side");
            string optionentered = Console.ReadLine();
            if (optionentered == "2D") {
                Console.WriteLine("Ok");
                Console.WriteLine("Enter the Base Area of the Cube");
                double ba = Convert.ToDouble(Console.ReadLine());
                Console.WriteLine("Enter a Height Measure");
                double height = Convert.ToDouble(Console.ReadLine());
                double volume = ba*height;
                Console.WriteLine("Volume of the Cube is " + volume);
            }
            else if (optionentered == "Side") {
                Console.WriteLine("Ok");
                Console.WriteLine("Enter the measure of the Side");
                double side = Convert.ToDouble(Console.ReadLine());
                double volume = Math.Pow(side, 3);
                Console.WriteLine("Volume of the Cube is " + volume);
            }
            else {
                Console.WriteLine("That's an invalid option. Try again later");
                Environment.Exit(0);
            }
    }
}
}
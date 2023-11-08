using System;

namespace VolumeOfCuboid 
{
    class Program 
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Do you wish to find the Volume of Cuboid by 2D Method or via 3D Method? Please enter either 2D or 3D")
            string option = Console.ReadLine();
            if (option == "2D") {
                Console.WriteLine("Ok");
                Console.WriteLine("Enter the Base Area of the Cuboid");
                double ba = Convert.ToDouble(Console.ReadLine());
                Console.WriteLine("Enter a Height Measure");
                double height = Convert.ToDouble(Console.ReadLine());
                double volume = ba*height;
                Console.WriteLine("Volume of the Cuboid is " + volume);
            }            
            else if (option == "3D") {
                Console.WriteLine("Ok");
                Console.WriteLine("Enter a Length Measure")
                double Length = Convert.ToDouble(Console.ReadLine());
                double Breadth = Convert.ToDouble(Console.ReadLine());
                double Height = Convert.ToDouble(Console.ReadLine());
                double volume = Length*Breadth*Height;
                Console.WriteLine("Volume of the Cuboid is " + volume);
            }
            else {
                Console.WriteLine("That's an invalid option. Try again later");
                Environment.Exit(0);
            }
        }
    }
}
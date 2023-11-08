using System;

namespace C__DataTypes
{
    class Program
    {
        static void Main(string[] args)
        {
            //Boolean is a Data Type where C# which has 2 values - True and False
            Console.WriteLine("Boolean Data Type");
            bool ifZeroTrue = false;
            Console.WriteLine(ifZeroTrue);
            bool ifOneTrue = true;
            Console.WriteLine(ifOneTrue);
            bool if15true = true;
            Console.WriteLine(if15true);
            bool ifnone = false;
            Console.WriteLine(ifnone);
            bool ifapos = false;
            Console.WriteLine(ifapos);

            Console.WriteLine("Float Data Type");
            float f1 = 0.5F;
            Console.WriteLine("Your number " + f1 + " is of type " + f1.GetType());
            float f2 = 1.5F;
            Console.WriteLine("Your number " + f2 + " is of type " + f2.GetType());            
            float f3 = 2.5F;
            Console.WriteLine("Your number " + f3 + " is of type " + f3.GetType());
            float f4 = 3.5F;
            Console.WriteLine("Your number " + f4 + " is of type " + f4.GetType());

            Console.WriteLine("Integer Data Type");
            int i1 = 0;
            Console.WriteLine("Your number " + i1 + " is of type " + i1.GetType());
            int i2 = 1;
            Console.WriteLine("Your number " + i2 + " is of type " + i2.GetType());
            int i3 = 2;
            Console.WriteLine("Your number " + i3 + " is of type " + i3.GetType());
            int i4 = 3;
            Console.WriteLine("Your number " + i4 + " is of type " + i4.GetType());

            Console.WriteLine("String Data Type");
            Console.WriteLine("Enter your Name");
            string s1 = Console.ReadLine();
            Console.WriteLine("Enter your Place of Birth");
            string s2 = Console.ReadLine();
            Console.WriteLine("Enter your Date of Birth");
            string s3 = Console.ReadLine();
            Console.WriteLine("Hello, " + s1 + ". You were born at " + s2 + ", on " + s3);
        }
    }
}

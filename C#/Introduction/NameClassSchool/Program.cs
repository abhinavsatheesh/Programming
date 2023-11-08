using System;

namespace NameClassSchool
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter your name");
            string name = Console.ReadLine();
            Console.WriteLine("Enter your class and division");
            string classdiv = Console.ReadLine();
            Console.WriteLine("Enter your school");
            string school = Console.ReadLine();
            Console.WriteLine("Your name is {0}", name);
            Console.WriteLine("Your class and division is {0}", classdiv);
            Console.WriteLine("Your school is {0}", school);
        }
    }
}

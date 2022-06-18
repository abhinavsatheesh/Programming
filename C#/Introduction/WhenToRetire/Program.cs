using System;

namespace WhenToRetire
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter your name");
            string name = Console.ReadLine();
            Console.WriteLine("Enter your age");
            int age = int.Parse(Console.ReadLine());
            Console.WriteLine("Enter your profession");
            string profession = Console.ReadLine();
            Console.WriteLine("Enter your retiring age");
            int retirementAge = int.Parse(Console.ReadLine());
            int yearsleft = retirementAge-age;
            Console.WriteLine("Hello " + name + ". Your age is " + age + ". You will have to retire from " + profession + " in " + yearsleft + " years.");
        }
    }
}

using System;

namespace C_Functions
{
    class Program
    {
        static void AskJob(string name, string job)
        {
            Console.WriteLine("Hello, " + name + ". Your job is " + job);
        }
        static void Main(string[] args)
        {
            Console.WriteLine("May I know your Name?");
            string name1 = Console.ReadLine();
            Console.WriteLine("May I know your job?");
            string job1 = Console.ReadLine();
            Program.AskJob(name1, job1);
        }
    }
}

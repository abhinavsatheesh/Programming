using System;
using System.Data;




namespace C__InBuiltModules
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Current Datetime");
            Console.WriteLine(DateTime.Now);

            Console.WriteLine("Evaluator");
            DataTable dt = new DataTable();
            var v = dt.Compute("10*10*10","");
            Console.WriteLine(v);

            Console.WriteLine("Execute");
            Console.WriteLine("Open Notepad");
            var p = System.Diagnostics.Process.Start("notepad");
            p.WaitForExit();
        }
    }
}

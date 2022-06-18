using System;
using System.IO;

class FileDirectory
{
    static void Main(String[] args)
    {
        string[] dirNames = Directory.GetDirectories(".");
        string[] fileNames = Directory.GetFiles(".");
        Console.WriteLine("Directories in " + Convert.ToString(System.Environment.CurrentDirectory) + "\n");
        foreach (string dirName in dirNames)
        {
            Console.WriteLine(dirName);
        }
        Console.WriteLine("\nFiles in " + Convert.ToString(System.Environment.CurrentDirectory) + "\n");
        foreach(string fileName in fileNames)
        {
            Console.WriteLine(fileName);
        }
    }
    

}
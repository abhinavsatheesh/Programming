using System;
using System.IO;
using System.Runtime.InteropServices;

class Program
{
    static void Main(String[] args)
    {
        if (RuntimeInformation.IsOSPlatform(OSPlatform.OSX))
        {
            Console.WriteLine("You are using a macOS System");
        }

        if (RuntimeInformation.IsOSPlatform(OSPlatform.Linux))
        {
            Console.WriteLine("You are using a Linux System");
        }

        if (RuntimeInformation.IsOSPlatform(OSPlatform.Windows))
        {
            Console.WriteLine("You are using a Windows System");
        }


    }
}
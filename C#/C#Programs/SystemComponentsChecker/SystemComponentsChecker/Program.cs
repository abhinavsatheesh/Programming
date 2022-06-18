using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;
using System.Management;
using System.IO;

namespace SystemComponentsChecker
{
    class Program
    {
        public static void Main()
        {
            GetOS();
            Console.WriteLine(System.Environment.MachineName);
            GetOSVersion();
            if (Environment.Is64BitOperatingSystem == true) {
                Console.WriteLine("Machine: x64");
            }
            else
            {
                Console.WriteLine("Machine: x86");
            }
            string path = Directory.GetCurrentDirectory();
            Console.WriteLine("Current Working Directory: " + path);
        }
        static void GetOS()
        {
            if (RuntimeInformation.IsOSPlatform(OSPlatform.OSX))
            {
                Console.WriteLine("System: macOS");
            }

            if (RuntimeInformation.IsOSPlatform(OSPlatform.Linux))
            {
                Console.WriteLine("System: Linux");
            }

            if (RuntimeInformation.IsOSPlatform(OSPlatform.Windows))
            {
                Console.WriteLine("System: Windows");
            }
        }
        static void GetOSVersion()
        {
            string r = "";
            using (ManagementObjectSearcher searcher = new ManagementObjectSearcher("SELECT * FROM Win32_OperatingSystem"))
            {
                ManagementObjectCollection information = searcher.Get();
                if (information != null)
                {
                    foreach (ManagementObject obj in information)
                    {
                        r = obj["Caption"].ToString() + " - " + obj["OSArchitecture"].ToString();
                    }
                }
                r = r.Replace("NT 5.1.2600", "XP");
                r = r.Replace("NT 5.2.3790", "Server 2003");
                Console.WriteLine("Version: " + r);
            }
        }
    }
}

using System;
using System.IO;

namespace PhotoOrganiser
{
    public class Program
    {
        #pragma warning disable
        public static void Main(string[] args)
        {
            string initialPath = "";
            string toPath = "";
            string option = "";
            Console.WriteLine("Welcome to Photo Organiser");
            while (true)
            {
                Console.WriteLine("Enter the Folder Path for checking the photos to organise");
                initialPath = Console.ReadLine();
                if (!Directory.Exists(initialPath))
                {
                    Console.WriteLine("Invalid Path Entered");
                    continue;
                }
                else
                {
                    break;
                }
            }
            
            while (true)
            {
                Console.WriteLine("Enter the Folder Path for copying the organised photos");
                toPath = Console.ReadLine();
                if (!Directory.Exists(initialPath))
                {
                    Console.WriteLine("Invalid Path Entered");
                    continue;
                }
                else
                {
                    break;
                }
            }   
            CheckAndOrganisePhotos(initialPath, toPath);
        }
        public static void CheckAndOrganisePhotos(string iniPath, string FiniPath)
        {
            string[] imagesInFolder = Directory.GetFiles(iniPath);
            if (!Directory.Exists(FiniPath))
            {
                Directory.CreateDirectory(FiniPath);
            }
            foreach (string image in imagesInFolder)
            {
                string taken_year = File.GetCreationTime(image).ToLongDateString().Split(" ")[2];
                if (!Directory.Exists(Path.Join(FiniPath, taken_year)))
                {
                    Directory.CreateDirectory(Path.Join(FiniPath, taken_year));
                }
                string taken_month = File.GetCreationTime(image).ToLongDateString().Split(" ")[1];
                if (!Directory.Exists(Path.Join(FiniPath, $"{taken_month} {taken_year}")))
                {
                    Directory.CreateDirectory(Path.Join(FiniPath, taken_year, $"{taken_month} {taken_year}"));
                }
                File.Copy(image, Path.Join(FiniPath, taken_year, $"{taken_month} {taken_year}", Path.GetFileName(image)));
            }
            Console.WriteLine($"All photos in {iniPath} have been organised and have been copied to {FiniPath}");
        }
    }
}
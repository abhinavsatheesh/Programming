using System;
using System.IO;
using System.Net;
using VideoLibrary;

class Program 
{
    #pragma warning disable 8600, 8604
    static void SaveVideoToDisk(string link)
    {
        var youTube = YouTube.Default; 
        var video = youTube.GetVideo(link); 
        File.WriteAllBytes(Path.Combine(Directory.GetCurrentDirectory(), video.FullName), video.GetBytes());
        Console.WriteLine("Video saved in the Path " + Directory.GetCurrentDirectory() + video.FullName);
    }
    static void Main(string[] args) 
    {
        Console.WriteLine("Enter the YouTube Video Link");
        string url = Console.ReadLine();
        SaveVideoToDisk(url);
    }
}
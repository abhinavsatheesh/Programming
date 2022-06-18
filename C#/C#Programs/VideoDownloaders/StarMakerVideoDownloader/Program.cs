using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Text;
using System.IO;
using System.Threading.Tasks;

namespace StarMakerVideoDownloader
{
    internal class Program
    {
        #pragma warning disable 8600, 8602, 8604, SYSLIB0014
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the URL of the File");
            string url = Console.ReadLine();
            HttpWebRequest webRequest = (HttpWebRequest)WebRequest.Create(url);
            webRequest.AllowAutoRedirect = false;  

            webRequest.Timeout = 10000;           
            webRequest.Method = "HEAD";
            HttpWebResponse webResponse;
            using (webResponse = (HttpWebResponse)webRequest.GetResponse())
            {
                if ((int)webResponse.StatusCode >= 300 && (int)webResponse.StatusCode <= 399)
                {
                    string uriString = webResponse.Headers["Location"];
                    string startSplit = uriString.Split("recordingId=")[1];
                    string recordingId = startSplit.Split("&")[0];
                    string toDownloadUrl = $"https://static.starmakerstudios.com/production/uploading/recordings/{recordingId}/master.mp4";
                    
                    using (var client = new WebClient())
                    {
                        client.DownloadFile(toDownloadUrl, "StarMakerVideo.mp4");
                    }
                    webResponse.Close();
                }
            }
            Console.WriteLine($"Downloaded Successfully in the Path " + Path.Combine(Directory.GetCurrentDirectory(), "StarMakerVideo.mp4"));
        }
    }
}

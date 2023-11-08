using System;
using System.IO;
using System.Net;
using System.Text;
using System.Collections.Specialized;
using System.Xml.Linq;

namespace ImgurExample
{
    class Program
    {
        #pragma warning disable 
        public static void Main(string[] args)
        {
            using (var w = new WebClient())
            {
                string clientID = "0dc6b4fbc159a6a";
                Console.WriteLine("Enter a File Name");
                string fileName = Console.ReadLine();
                string fileExtension = Path.GetExtension(fileName);
                w.Headers.Add("Authorization", "Client-ID " + clientID);
                var values = new NameValueCollection
                {
                    { "image", Convert.ToBase64String(File.ReadAllBytes(fileName)) }
                };
                byte[] response = w.UploadValues("https://api.imgur.com/3/upload.xml", values);
                var review = XDocument.Load(new MemoryStream(response));
                string url = (review.Root.Element("link").Value).Replace(fileExtension, ".webp?maxwidth=640&shape=thumb&fidelity=medium");
                Console.WriteLine(url);
            }
        }
    }
}
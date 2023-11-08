using System.Collections.Specialized;
using System.Net;
using System.Text.Json;
using System.Net.Http;
using System.Diagnostics;
using System.Xml.Linq;


namespace TempleNotebook
{
#pragma warning disable
    public partial class Form1 : Form
    {
        public class TempleFormatWithoutImages
        {
            public string TempleName { get; set; }
            public string TempleDetails { get; set; }
            
        }
        public class TempleFormatWithImages
        {
            public string TempleName { get; set; }
            public string TempleDetails { get; set; }
            public string[] AddedImages { get; set; }
        }
        public Form1()
        {
            InitializeComponent();
        }

        private async void button1_Click(object sender, EventArgs e)
        {
            string templename = textBox1.Text;
            string completenote = richTextBox1.Text;
            string[] files = openFileDialog1.FileNames;
            List<string> main_Images = new List<string> { };
            List<string> list = new List<string>(files);
            list.Remove("openFileDialog1");
            string[] completeFiles = list.ToArray();
            if (completeFiles.Length == 0)
            {
                var format = new TempleFormatWithoutImages
                {
                    TempleName = templename,
                    TempleDetails = completenote
                };
                string jsonstring = JsonSerializer.Serialize(format);
                var jsonsss = new StringContent(jsonstring);
                HttpClient httpClient = new HttpClient();
                var response = httpClient.PatchAsync($"https://temple-notebook-1640359038869-default-rtdb.firebaseio.com/{templename}.json", jsonsss).Result;
                MessageBox.Show("Temple Note has been added successfully", "Temple Note Added");
                textBox1.Text = "";
                richTextBox1.Text = "";
            }
            else
            {
                foreach(string file in completeFiles)
                {
                    using (var w = new WebClient())
                    {
                        string clientID = "0dc6b4fbc159a6a";
                        string fileExtension = Path.GetExtension(file);
                        w.Headers.Add("Authorization", "Client-ID " + clientID);
                        var values = new NameValueCollection
                        {
                            { "image", Convert.ToBase64String(File.ReadAllBytes(file)) }
                        };
                        byte[] response = w.UploadValues("https://api.imgur.com/3/upload.xml", values);
                        var review = XDocument.Load(new MemoryStream(response));
                        string url = (review.Root.Element("link").Value).Replace(fileExtension, ".webp?maxwidth=640&shape=thumb&fidelity=medium");
                        main_Images.Add(url);
                        Debug.WriteLine(url);
                    }
                }
                string[] images = main_Images.ToArray();

                var format = new TempleFormatWithImages
                {
                    TempleName = templename,
                    TempleDetails = completenote,
                    AddedImages = images
                };
                string jsonstring = JsonSerializer.Serialize(format);
                var jsonsss = new StringContent(jsonstring);
                HttpClient httpClient = new HttpClient();
                var response_1 = httpClient.PatchAsync($"https://temple-notebook-1640359038869-default-rtdb.firebaseio.com/{templename}.json", jsonsss).Result;
                MessageBox.Show("Temple Note has been added successfully", "Temple Note Added");
                textBox1.Text = "";
                richTextBox1.Text = "";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            openFileDialog1.ShowDialog();
        }
    }
}
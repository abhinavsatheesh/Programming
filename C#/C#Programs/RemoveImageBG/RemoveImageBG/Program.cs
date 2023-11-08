using System;

class Program
{
    static void Main(String[] args)
    {
        Console.WriteLine("Enter the Path of the File");
        string FilePath = Console.ReadLine();
        string FileName = Path.GetFileName(FilePath);
        string FolderName = Path.GetDirectoryName(FilePath);
        string ToSavePath = Path.Combine(FolderName, "no-bg.png");
        using (var client = new HttpClient())
        using (var formData = new MultipartFormDataContent())
        {
            formData.Headers.Add("X-Api-Key", "BeoTpZimF517Xc2vFsAN1HLY");
            formData.Add(new ByteArrayContent(File.ReadAllBytes(FilePath)), "image_file", FileName);
            formData.Add(new StringContent("auto"), "size");
            var response = client.PostAsync("https://api.remove.bg/v1.0/removebg", formData).Result;

            if (response.IsSuccessStatusCode)
            {
                FileStream fileStream = new FileStream(ToSavePath, FileMode.Create, FileAccess.Write, FileShare.None);
                response.Content.CopyToAsync(fileStream).ContinueWith((copyTask) => { fileStream.Close(); });
            }
            else
            {
                Console.WriteLine("Error: " + response.Content.ReadAsStringAsync().Result);
            }
        }
    }
}


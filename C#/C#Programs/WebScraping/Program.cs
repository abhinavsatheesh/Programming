using CsvHelper;
using HtmlAgilityPack;
using System.IO;
using System.Collections.Generic;
using System.Globalization;

public class Row
{
    public string Title {get; set;}
}

class Program
{
    static void Main(string[] args)
    {
        HtmlWeb web = new HtmlWeb();
        HtmlDocument doc = web.Load("https://en.wikipedia.org/wiki/Greece");
        var HeaderNames = doc.DocumentNode.SelectNodes("//span[@class='toctext']");
        var titles = new List<Row>();
        foreach (var item in HeaderNames)
        {
            titles.Add(new Row { Title = item.InnerText});
        }
        using (var writer = new StreamWriter("./ScrapedData.csv"))
        using (var csv = new CsvWriter(writer, CultureInfo.InvariantCulture))
        {
            csv.WriteRecords(titles);
        }
        Console.WriteLine("Scraped Data saved in " + Directory.GetCurrentDirectory() + "/ScrapedData.csv");
    }
}
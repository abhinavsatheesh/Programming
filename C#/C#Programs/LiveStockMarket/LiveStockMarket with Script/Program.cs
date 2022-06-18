using System;
using System.Net;
using System.IO;
using System.Reflection;

class Program
{
    #pragma warning disable CS8600
    static void Main(string[] args)
    {
        Console.WriteLine("Enter a Stock Symbol according to Google Finance");
        string symbol = Console.ReadLine();
        string fullUrl = $"https://www.google.com/finance/quote/{symbol}:NSE";
        HttpClient client = new HttpClient();
        var response = client.GetStringAsync(fullUrl);
        HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
        doc.LoadHtml(response.Result);
        HtmlAgilityPack.HtmlNode htmlDoc = doc.DocumentNode;
        HtmlAgilityPack.HtmlNode node = htmlDoc.SelectSingleNode("//div[@class='YMlKec fxKbKc']");
        try
        {
            string StockPrice = (node.InnerText).Split("₹")[1];
            Console.WriteLine($"Stock Price of {symbol} is Rs. {StockPrice}");
        }
        catch 
        {
            Console.WriteLine("Invalid Symbol");
        }
    }
}
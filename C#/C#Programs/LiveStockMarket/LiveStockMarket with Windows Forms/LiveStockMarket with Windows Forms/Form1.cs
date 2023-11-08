using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Net;
using System.IO;
using System.Reflection;
using System.Drawing;
using Newtonsoft.Json;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Net.Http;

namespace LiveStockMarket_with_Windows_Forms
{
    
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            ShareList myList = new ShareList();
            string[] ListOfShares = myList.SHARES;
            AutoCompleteStringCollection allowedTypes = new AutoCompleteStringCollection();
            allowedTypes.AddRange(ListOfShares);
            textBox1.AutoCompleteCustomSource = allowedTypes;
            textBox1.AutoCompleteMode = AutoCompleteMode.Suggest;
            textBox1.AutoCompleteSource = AutoCompleteSource.CustomSource;
            textBox2.AutoCompleteCustomSource = allowedTypes;
            textBox2.AutoCompleteMode = AutoCompleteMode.Suggest;
            textBox2.AutoCompleteSource = AutoCompleteSource.CustomSource;
        }
        private void GetSharePrice(string symbolName, Label labelName)
        {
            string symbol = symbolName;
            if (symbol == "NIFTY 50")
            {
                string fullUrlNifty = "https://www.google.com/finance/quote/NIFTY_50:INDEXNSE";
                HttpClient clientNifty = new HttpClient();
                var responseNifty = clientNifty.GetStringAsync(fullUrlNifty);
                HtmlAgilityPack.HtmlDocument docNifty = new HtmlAgilityPack.HtmlDocument();
                docNifty.LoadHtml(responseNifty.Result);
                HtmlAgilityPack.HtmlNode htmlDocNifty = docNifty.DocumentNode;
                HtmlAgilityPack.HtmlNode nodeNameNifty = htmlDocNifty.SelectSingleNode("//div[@class='zzDege']");
                HtmlAgilityPack.HtmlNode nodePriceNifty = htmlDocNifty.SelectSingleNode("//div[@class='YMlKec fxKbKc']");
                try
                {
                    string StockPrice = (nodePriceNifty.InnerText);
                    string CompanyName = (nodeNameNifty.InnerText);
                    labelName.Text = ($"Stock Price of {CompanyName} is Rs. {StockPrice}");
                }
                catch
                {
                    MessageBox.Show("An unhandled exception error occured. Try again later or try again with another stock symbol", "An error occured", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
            else if (symbol == "NIFTY")
            {
                string fullUrlNifty = "https://www.google.com/finance/quote/NIFTY_50:INDEXNSE";
                HttpClient clientNifty = new HttpClient();
                var responseNifty = clientNifty.GetStringAsync(fullUrlNifty);
                HtmlAgilityPack.HtmlDocument docNifty = new HtmlAgilityPack.HtmlDocument();
                docNifty.LoadHtml(responseNifty.Result);
                HtmlAgilityPack.HtmlNode htmlDocNifty = docNifty.DocumentNode;
                HtmlAgilityPack.HtmlNode nodeNameNifty = htmlDocNifty.SelectSingleNode("//div[@class='zzDege']");
                HtmlAgilityPack.HtmlNode nodePriceNifty = htmlDocNifty.SelectSingleNode("//div[@class='YMlKec fxKbKc']");
                try
                {
                    string StockPrice = (nodePriceNifty.InnerText);
                    string CompanyName = (nodeNameNifty.InnerText);
                    labelName.Text = ($"Stock Price of {CompanyName} is Rs. {StockPrice}");
                }
                catch
                {
                    MessageBox.Show("Invalid symbol. Please try again", "Stock not found", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
            else if (symbol == "NSE")
            {
                string fullUrlNifty = "https://www.google.com/finance/quote/NIFTY_50:INDEXNSE";
                HttpClient clientNifty = new HttpClient();
                var responseNifty = clientNifty.GetStringAsync(fullUrlNifty);
                HtmlAgilityPack.HtmlDocument docNifty = new HtmlAgilityPack.HtmlDocument();
                docNifty.LoadHtml(responseNifty.Result);
                HtmlAgilityPack.HtmlNode htmlDocNifty = docNifty.DocumentNode;
                HtmlAgilityPack.HtmlNode nodeNameNifty = htmlDocNifty.SelectSingleNode("//div[@class='zzDege']");
                HtmlAgilityPack.HtmlNode nodePriceNifty = htmlDocNifty.SelectSingleNode("//div[@class='YMlKec fxKbKc']");
                try
                {
                    string StockPrice = (nodePriceNifty.InnerText);
                    string CompanyName = (nodeNameNifty.InnerText);
                    labelName.Text = ($"Stock Price of {CompanyName} is Rs. {StockPrice}");
                }
                catch
                {
                    MessageBox.Show("Invalid symbol. Please try again", "Stock not found", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
            else if (symbol == "SENSEX")
            {
                string fullUrlNifty = "https://www.google.com/finance/quote/SENSEX:INDEXBOM";
                HttpClient clientNifty = new HttpClient();
                var responseNifty = clientNifty.GetStringAsync(fullUrlNifty);
                HtmlAgilityPack.HtmlDocument docNifty = new HtmlAgilityPack.HtmlDocument();
                docNifty.LoadHtml(responseNifty.Result);
                HtmlAgilityPack.HtmlNode htmlDocNifty = docNifty.DocumentNode;
                HtmlAgilityPack.HtmlNode nodeNameNifty = htmlDocNifty.SelectSingleNode("//div[@class='zzDege']");
                HtmlAgilityPack.HtmlNode nodePriceNifty = htmlDocNifty.SelectSingleNode("//div[@class='YMlKec fxKbKc']");
                try
                {
                    string StockPrice = (nodePriceNifty.InnerText);
                    string CompanyName = (nodeNameNifty.InnerText);
                    labelName.Text = ($"Stock Price of {CompanyName} is Rs. {StockPrice}");
                }
                catch
                {
                    MessageBox.Show("Invalid symbol. Please try again", "Stock not found", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
            else if (symbol == "BSE")
            {
                string fullUrlNifty = "https://www.google.com/finance/quote/SENSEX:INDEXBOM";
                HttpClient clientNifty = new HttpClient();
                var responseNifty = clientNifty.GetStringAsync(fullUrlNifty);
                HtmlAgilityPack.HtmlDocument docNifty = new HtmlAgilityPack.HtmlDocument();
                docNifty.LoadHtml(responseNifty.Result);
                HtmlAgilityPack.HtmlNode htmlDocNifty = docNifty.DocumentNode;
                HtmlAgilityPack.HtmlNode nodeNameNifty = htmlDocNifty.SelectSingleNode("//div[@class='zzDege']");
                HtmlAgilityPack.HtmlNode nodePriceNifty = htmlDocNifty.SelectSingleNode("//div[@class='YMlKec fxKbKc']");
                try
                {
                    string StockPrice = (nodePriceNifty.InnerText);
                    string CompanyName = (nodeNameNifty.InnerText);
                    labelName.Text = ($"Stock Price of {CompanyName} is Rs. {StockPrice}");
                }
                catch
                {
                    MessageBox.Show("Invalid symbol. Please try again", "Stock not found", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
            else
            {
                string fullUrl = $"https://www.google.com/finance/quote/{symbol}:NSE";
                HttpClient client = new HttpClient();
                var response = client.GetStringAsync(fullUrl);
                HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
                doc.LoadHtml(response.Result);
                HtmlAgilityPack.HtmlNode htmlDoc = doc.DocumentNode;
                HtmlAgilityPack.HtmlNode nodeName = htmlDoc.SelectSingleNode("//div[@class='zzDege']");
                HtmlAgilityPack.HtmlNode nodePrice = htmlDoc.SelectSingleNode("//div[@class='YMlKec fxKbKc']");
                try
                {
                    string StockPrice = (nodePrice.InnerText).Split('₹')[1];
                    string CompanyName = (nodeName.InnerText);
                    labelName.Text = ($"Stock Price of {CompanyName} is Rs. {StockPrice}");
                }
                catch
                {
                    MessageBox.Show("Invalid symbol. Please try again", "Stock not found", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
        }
        private void linkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            System.Diagnostics.Process.Start("https://google.com/finance");
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string symbol = textBox1.Text;
            GetSharePrice(symbol, label5);   
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string symbol = textBox2.Text;
            GetSharePrice(symbol, label6);
        }
    }
}

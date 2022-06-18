using System;
using System.Net;
using (var client = new WebClient())
{
    client.DownloadFile("https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png", "GoogleLogo.png");
}

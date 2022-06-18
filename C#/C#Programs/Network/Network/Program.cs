using System;
using System.Net;
using System.Net.Sockets;

namespace Network
{
    class Program
    {
        static void Main(string[] args)
        {
            string hostname = Dns.GetHostName();
            string localIP = string.Empty;
            using (Socket socket = new Socket(AddressFamily.InterNetwork, SocketType.Dgram, 0))
            {
                socket.Connect("8.8.8.8", 65530);
                IPEndPoint endPoint = socket.LocalEndPoint as IPEndPoint;
                localIP = endPoint.Address.ToString();
            }
            Console.WriteLine("Host Name : " + hostname);
            Console.WriteLine("IP Address : " + localIP);
        }
    }
}

using System;

namespace FindingTheCostOfAnItem
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the name of the Item");
            string name = Console.ReadLine();
            Console.WriteLine("Enter the quantity of the Item. Enter in Kilograms");
            double quantity = int.Parse(Console.ReadLine());
            Console.WriteLine("Enter the price of the Item");
            double sprice = int.Parse(Console.ReadLine());
            double totalprice = quantity*sprice;
            Console.WriteLine("Total Price for the Item " + name + " is Rs. " + totalprice);
        }
    }
}

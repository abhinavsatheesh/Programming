﻿using System;

namespace C_Loops
{
    class Program
    {
        static void Main()
        {
            int[] numbers = {1, 2, 3, 4, 5};
            foreach (int number in numbers)
            {
                Console.WriteLine(number*4);
            }
        }
    }
}

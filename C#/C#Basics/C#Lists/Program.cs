using System;
using System.Linq;

public static class Extensions
{
    public static T[] Append<T>(this T[] array, T item)
    {
        if (array == null) {
            return new T[] { item };
        }
        T[] result = new T[array.Length + 1];
        array.CopyTo(result, 0);
        result[array.Length] = item;
        return result;
    }
}

class StringToFloat {
  static void Main(string[] args) {

    string[] myArray = {"Python", "C++", "JavaScript", "HTML", "CSS"};
    Console.WriteLine("Hi. Your list is:");
    foreach(string value in myArray) {
      Console.WriteLine(value);
    }
    Console.WriteLine("\nRemoving C++");
    int indexToRemove = 1;
    myArray = myArray.Where((source, index) =>index != indexToRemove).ToArray();
    Console.WriteLine("Updated List is:");
    foreach(string value in myArray) {
      Console.WriteLine(value);
    }
    Console.WriteLine("\nAdding Java");
    string[] newArray = myArray.Append("Java");
    Console.WriteLine("Updated List is:");
    foreach(string value in newArray) {
      Console.WriteLine(value);
    }
  }
}

using System;
using System.Collections;
using System.Linq;

namespace Lessons
{
  class Program
  {
    static void Main(string[] args)
    {
      int[] myArray = new int[10];
      Random random = new Random();
      for(int i = 0;i<myArray.Length;i++)
      {
        myArray[i] = random.Next(100,999);
        Console.Write($"{myArray[i]}"+"\t");
      }
      Console.WriteLine();
    }
  }
}

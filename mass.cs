using System;
using System.Collections;
using System.Linq;

namespace Lessons
{
  class Program
  {
    static void Main(string[] args)
    {
      int[,] myArray = new int[6,7];
      Random random = new Random();
      for(int i = 0;i<myArray.GetLength(0);i++)
      {
      	for(int j = 0; j < myArray.GetLength(1); j++)
	{
        	myArray[i,j] = random.Next(10,999);
        	Console.Write($"{myArray[i,j]}"+"\t");
	}
      }
      Console.WriteLine();
    }
  }
}

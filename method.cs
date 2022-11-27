using System;
using System.Collections.Generic;
using System.Linq;

namespace lessons
{
  class My
  {
    public void Arr()
    {
      int[][] myArray = new int[3][];
      myArray[0] = new int[2];
      myArray[1] = new int[8];
      myArray[2] = new int[6];
      for (int i =0; i < myArray.Length;i++)
      {
        for (int j = 0; j< myArray[i].Length;j++)
        {
          myArray[i][j] = (i + 1) * (j + 1);
        }
      }
      for (int i = 0; i < myArray.Length; i++)
      {
        for (int j = 0; j< myArray[i].Length;j++)
        {
          Console.Write($"{myArray[i][j]}"+"\t");
        }
        Console.WriteLine();
      }
    }
  }
  class Program
  {
    static void Main(string[] args)
    {
      My my = new My();
      my.Arr();
      Console.WriteLine();
    }
  }
}

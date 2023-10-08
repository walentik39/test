#include <iostream>
#include <ctime>

using namespace std;

int main()
{
	srand(time(NULL));
	for(int i=0; i <12; i++)
		for (int j=i+1; j<rand()%10;j++)
		{
			int a = rand()%10;
			cout << a << endl;
			int b = rand()%100;
			cout<< b <<'\t'<< endl;
		}
}

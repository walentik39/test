#include <iostream>
#include <math.h>

using namespace::std;

int main()
{
	for(int i=0;i<=25;i++)
	{
		if(i%2==0)
			cout<<i<<endl;
		else
			cout<<double(sqrt(i))<<endl;
	}
	return 0;
}

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int a;
	int b;
	printf("Введите первое число ");
	scanf("%d",&a);
	scanf("%d",&b);
	int event = 0;
	while(a<b)
	{
		if(a%2==0)
			event ++;
		a++;
	}
	printf("%d чётных чисел: \n",event);
	return 0;
}

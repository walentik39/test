#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main(int argc, const char* argv[])
{
	int n;
	scanf("%d", &n);
	for (int i  = 0; i < n; i++)
	{
		printf("#\t");
	}
		for( int j= 5; j>0; j--)
			printf("*\n");
	return 0;
}

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(void)
{
	int n;
	scanf("%d", &n);
	for(int i  = 0; i < n; i++)
		printf("*\n");
	for( int j= n; j>0; j--)
		printf("#\t");
	return 0;
}

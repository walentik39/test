#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
void golaction(int i)
{
	if (i == 0)
	{
		printf("LIKE\n");
	}
	else{
	printf("%d\n", i);
	golaction(i - 1);
	}
	return;
}
int main(void)
{
	int n;
	scanf("%d",&n);
	golaction(n);
	return 0;
}

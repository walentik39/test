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
int main(int argc, char* argv[])
{
	golaction(8);
	return 0;
}

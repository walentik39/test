#include <stdio.h>
#include <stdlib.h>

long int factorial(long int n)
{
	if(n == 0 || n == 1) return 1;
	return n * factorial(n - 1);
}

int main(int argc, char* argv[])
{
	unsigned long int n;
	printf("Calculation n!\nInput n: ");
	scanf("%lu", &n);
	if (n >=0)
		printf("%d! = %d\n", n, factorial(n));
	else
		printf("Error . n must be >= 0\n");
	return 0;
}

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
	float a, b;
	printf("Введите первое число:");
	scanf("%f", &a);
	printf("введите второе число:");
	scanf("%f", &b);
	printf("%f\n", (a - b)/b);
	return 0;
}

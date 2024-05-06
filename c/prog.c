#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <math.h>

int main(void)
{
	double a, b;
	printf("Введите первое число: ");
	scanf("%lf", &a);
	printf("введите второе число: ");
	scanf("%lf", &b);
	if (a > b)
	{
		printf("%lf\n",(b/(a/100)));
	}
	else
		printf("%lf\n", (a/(b/100)));
	return 0;
}

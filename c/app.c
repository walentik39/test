#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int sum(int, int);

int sub(int, int);

int mul(int, int);

double div_d(double, double);

int sum(int a, int b)
{
	return a + b;
}
int sub(int a, int b)
{
	return a - b;
}
int mul(int a, int b)
{
	return a * b;
}
double div_d(double a, double b)
{
	return a / b;
}


int main(void)
{
	printf("Div: %lf\n", div_d(139,13));
	printf("Sum: %i\n", sum(12, 66));
	printf("Sub: %i\n", sub(56,77));
	printf("Mul: %i\n", mul(12,33));
	return 0;
}

#include <stdio.h>
#include <stdlib.h>

int main()
{
	int fahr, celsius;
	int lower, upper, step;
	lower = 0; /* нижняя граница таблицы температур */
	upper = 300; /* верхняя граница */
	step = 10;
	fahr = lower;
	while (fahr <= upper) {
		celsius = 5 * (fahr-32) / 9;
		printf("%d\t %d\n", fahr, celsius);
		fahr = fahr + step;
	}
	EXIT_SUCCESS;
}

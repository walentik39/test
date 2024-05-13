#include <time.h>
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	srand(time(NULL));
	time_t seconds;
	time(&seconds);

	while (1) {
		int r = rand() % 30;
		printf("%d %ld\n ", r, seconds);
		if (r == 22) {
			break;
		}
	}
	printf("\n");
	return 0;
}

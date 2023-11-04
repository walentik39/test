#include <time.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
	srand(time(NULL));

	while (1) {
		int r = rand() % 30;
		printf("%d ", r);
		if (r == 22) {
			break;
		}
	}
	printf("\n");
	return 0;
}

#include <stdio.h>
#include <stdlib.h>
#include <string.h>


enum colors {red, green, blue};
enum {
	go = 0x1f00,
	stop = 0x0001,
	forward = go,
	run = 0x00a2,
	back = run - 1
} first, two;

int main(void)
{
	printf("red>>1 = %d\n,green>>1 = %d, blue>>1 = %d\n",red>>1,green>>1,blue>>1);
	printf("red = %d, green = %d, blue = %d\n", red, green, blue);
	printf("first = %d, two = %d\n", go, back);
	return 0;
}

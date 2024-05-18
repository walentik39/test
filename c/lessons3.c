#include <stdio.h>
#include <stdlib.h>

struct tag_point {
	int x;
	int y;
	int z;
};

int main(void)
{

	struct tag_point pt = {10, 20, 30};

	printf("x = %d, y = %d, z = %d\n", pt.x, pt.y, pt.z);

	struct tag_point pt2 = {.y = 10, .z = 44, .x = 8};

	printf("x = %d, y = %d, z = %d\n", pt2.x, pt2.y, pt2.z);
	return 0;
}

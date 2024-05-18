#include <stdio.h>
#include <stdlib.h>

struct tag_point {
	int x;
	int y;
	int z;
};

int main(void)
{
	struct tag_point pt;
	pt.x = 12;
	pt.y = 22;
	pt.z = 33;

	printf("x = %d, y = %d, z = %d\n", pt.x, pt.y, pt.z);

	return 0;
}

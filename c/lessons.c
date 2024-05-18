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

	size_t sz_pt = sizeof(pt);
	size_t sz_st = sizeof(struct tag_point);
	printf("sz_pt = %ld, sz_st = %ld\n", sz_pt, sz_st);

	return 0;
}

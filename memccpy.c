#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int aprc, char* argv[])
{
	unsigned char src[15] ="1234567890";

	unsigned char dst[15] = "";

	memccpy (dst, src, '7', 10);
	fprintf(stdout,"dst: %s\n", dst);

	EXIT_SUCCESS;
}

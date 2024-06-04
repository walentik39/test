#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void func()
{
	signed short a;
	signed short b;
	for (a = 0; a < 12; a++)
		printf("%d\n", a);
	b = a;
	for (; b>=0 ; b--)
		printf("%d\n",b);
}

int main()
{
	func();
	return 0;
}

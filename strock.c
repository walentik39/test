#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SIZE 51

int main(int argc, char* argv[])
{
	char symbol = 'A';
	for (;symbol <='z'; symbol++)
		fprintf(stdout, "%c ", symbol);
	fprintf(stdout, "\n");
	char symbol_ = '0';
	for (;symbol_ <= '9'; symbol_++)
		fprintf(stdout, "%c ", symbol_);
	fprintf(stdout, "\n");
	EXIT_SUCCESS;
}

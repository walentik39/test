#include <stdio.h>
#include <stdlib.h>
#include <string.h>

enum {name_length=50, b_length=20};

struct tag_fio {
	char name[name_length];
	char last[name_length];
};

struct tag_person {
	struct tag_fio fio;
	char sex;
	unsigned short old;
	char b_date[b_length];
};

int main(void)
{

	struct tag_person person = {
		{"Alzoba","Walentin"},
		'M',
		53,
		"17.04.1971"
	};	
	person.old = 17;
	strcpy(person.b_date, "31.12.2012");


	printf("sex : %c, old : %d, b_date: %s\n", person.sex, person.old, person.b_date);
	printf("name: %s, last: %s\n", person.fio.name, person.fio.last);
	return 0;
}

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
        struct tag_person p;
	p = person;
        
	printf("sex : %c, old : %d, b_date: %s\n", p.sex, p.old, p.b_date);
	printf("name: %s, last: %s\n", p.fio.name, p.fio.last);
	return 0;
}

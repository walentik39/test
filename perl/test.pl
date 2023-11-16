#!/usr/bin/perl -W

$a=0;
while ($a<100)
{

	print "$a\n";
	$a=$a+3;
	sleep(1);
	if($a % 2 == 0)
	{
		print("$a\t");
	}
}

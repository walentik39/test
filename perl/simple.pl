#!/usr/bin/perl

use 5.30.0;
use warnings;

my @vals = (1, 2, 3, 4, 5, 6);

say $vals[0];
say $vals[1];
say $vals[-1];

$vals[6] = 7;
$vals[7] = 8;

$, = ' ';
say @vals;

my $n = @vals;

say "\@vals has $n elements"; 

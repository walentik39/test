#!/usr/bin/perl

use 5.30.0;
use warnings;
use Data::Dumper qw(Dumper);

die "Usage: $0 arg1 arg2 arg3\n" if @ARGV < 3;

say $ARGV[0];
say $ARGV[2];

say Dumper \@ARGV;



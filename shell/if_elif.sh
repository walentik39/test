#!/usr/bin/env bash
#if elif statement
read -p "Enter the marks: " marks

if (( $marks >= 90 )); then
	echo "Grade is A+ "
elif (( $marks < 90 && $marks >= 80 )); then
	echo "Grade is A "
elif (( $marks < 80 && $marks >= 70 )); then
	echo "Grade is B+ "
elif (( $marks < 70 && $marks >= 60 )); then
	echo "Grade is C"
else
	echo "Gade is F"
fi

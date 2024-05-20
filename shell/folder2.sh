#!/usr/bin/env bash
touch file.md
IFS=:
FUNC=$(host localhost)
for FOLDER in $FUNC
do
	echo "$FOLDER:" >> file.md
	for file in $FOLDER/*.*
	do
		if [ -x $file ]
		then
			echo " $file" >> file.md
		fi
	done
done

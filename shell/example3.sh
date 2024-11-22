#!/usr/bin/env bash

set -eExu

echo -n "Введите команду : "
read com
if $com 
then
	echo "Верно!"
	exit 0
else
	echo "Ошибка!"
	exit 1
fi


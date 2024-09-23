#!/usr/bin/env bash
read -p "Enter the age: " age
if [ $age -lt 20 ]; then
	echo "Вы ещё молоды"
fi
if [ $age -gt 100 ]; then
	echo "Вы прекрасно держитесь"
fi


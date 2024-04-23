#!/usr/bin/bash

while true; do
	BAT=$(acpi -s | cut -d' ' -f4 | sed 's/.$//' | sed 's/.$//')

	if [ $BAT -le 20 ]
	then
		notify-send 'Низкий уровень зараяда батареи!'
		sleep 60s
	fi
	sleep 5s
done &

# при наличии проги acpi 

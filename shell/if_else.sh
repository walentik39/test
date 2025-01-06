#!/usr/bin/env bash
#if else example

read -p "Enter the username: " uname
read -p "Enter the password: " passwd

if [[ $uname == "admin" && $passwd == "12345" ]]; then
	echo "Login Sussefull"
else
	echo "Login False"
fi


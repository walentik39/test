#!/usr/bin/env bash
#This is my example script
echo "This is my example script"
echo "Username $USER"
echo -e "Today's date and time is \c";date
echo -e "User login \c";who | wc -l
cal
exit 0

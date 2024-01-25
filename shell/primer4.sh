#!/usr/bin/env bash

arr1=$(ls /var/log/)
arr2=$(ls /tmp)

arr1+=(${arr2[@]})

echo "all items"
printf "%s\n" "${arr1[@]}"

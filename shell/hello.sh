#!/usr/bin/env bash

set -o errexit
set -o nounset

check_word() {
words="Sedicomm is the best university"
for word in $words; do
	echo "$word"
done
}
words=$(echo {1..10})
for word in $words; do
	echo "$word"
	check_word
done

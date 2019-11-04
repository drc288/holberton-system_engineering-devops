#!/usr/bin/env bash
# This script verify if the file exists
f="holbertonschool"
if [ -e "$f" ]; then
	echo "holbertonschool file exists"
	if [ -s "$f" ]; then
		echo "holbertonschool file is not empty"
	else
		echo "holbertonschool file is empty"
	fi

	if [ -f "$f" ]; then
		echo "holbertonschool is a regular file"
	fi
else
	echo "holbertonschool file does not exist"
fi

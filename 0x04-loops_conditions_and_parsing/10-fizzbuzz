#!/usr/bin/env bash
# Fizz Buzz!
i="1"
while [ $i -le "100" ]; do
	if [[ $((i % "3")) -eq "0" && $((i % "5")) -eq "0" ]]; then
		echo "FizzBuzz"
		i=$((i + 1))
	fi
	if [[ $((i % "3")) -eq "0" ]]; then
		echo "Fizz"
		i=$((i + 1))
	fi
	if [[ $((i % 5)) -eq "0" ]]; then
		echo "Buzz"
		i=$((i + 1))
	fi
	echo $i
	i=$((i + 1))
done

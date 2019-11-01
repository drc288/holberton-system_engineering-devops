#!/usr/bin/env bash
# This script is displaying "Holberton School" 10 times
# print in position 4 bad luck
# print in position 8 good luck
# for the most curiuos;
# good luck - https://intranet.hbtn.io/rltoken/fiGm-P2Yj-ljaNG-d6WJWA
# bad luck - https://intranet.hbtn.io/rltoken/yVebRHCOdVy08j5Fylv5lQ
i="0"
while [ $i -lt "10" ]; do
	if ((i == "3")); then
                 echo "bad luck"
                 i=$((i + 1))
	   elif ((i == "7")); then
		   echo "good luck"
		   i=$((i + 1))
	   else
                 echo "Holberton School"
                 i=$((i + 1))
       fi
done

#!/bin/bash
j=0
for (( i = 0; i <= 99; i++ )); do
	if [ $j -lt 10 ];
	then
		let "j++";
	fi;

	if [ $i -lt 10 ]; then
		echo -e "\x030,"$i" "$i"  \x03\c";
	fi;
	if [ $i -gt 9 ]; then
		if [ $i -lt 100 ]; then
			echo -e "\x030,"$i" "$i" \x03\c";
		fi;
	fi;
	if [ $j -eq 10 ]; then
		echo ""; j=0;
	fi;
done

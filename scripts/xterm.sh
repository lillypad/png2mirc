#!/bin/bash
j=0
for (( i = 0; i <= 255; i++ )); do
	if [ $j -lt 10 ];
	then
		let "j++";
	fi;
	if [ $i -lt 10 ];
	then
		echo -e "\e[48;5;"$i"m"$i"    \e[0m\c";
	fi;
	if [ $i -gt 9 ]; then
		if [ $i -lt 100 ]; then
			echo -e "\e[48;5;"$i"m"$i"   \e[0m\c";
		fi;
	fi;
	if [ $i -gt 99 ]; then
		echo -e "\e[48;5;"$i"m"$i"  \e[0m\c";
	fi;
	if [ $j -eq 10 ]; then
		echo ""; j=0;
	fi;
done
echo ""

#!/bin/bash

set -e

xmax=$1
ymax=$1

points() {
    xmax=$1
    ymax=$2
    
    for x in $(seq 0 "$xmax"); do
	for y in $(seq 0 "$ymax"); do
	    echo "$x,$y"
	done
    done
}

cwd=$(dirname "$0")
machinefile="$cwd"/machines.list
workdir="$cwd"/workdata
declare -A machines
i=1
for machine in $(cat "$machinefile"); do
    : > "$workdir"/$machine
    machines[$i]=$machine
    ((i++))
done

i=1
for point in $(points "$xmax" "$ymax"); do
    echo "$point" >> "$workdir"/"${machines[$i]}"
    ((i++))
    if [ -z ${machines[$i]} ]; then
	i=1
    fi
done

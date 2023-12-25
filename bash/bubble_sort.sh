#!/bin/bash

bubble_sort() {
  local -n arr=$1
  local len=${#arr[@]}
  local i j temp
  ``
  for ((i=0; i<$len; i++)); do
    for ((j=0; j<$len-i-1; j++)); do
        if [[ ${arr[$j]} -gt ${arr[$j+1]} ]]; then
            temp=${arr[$j]}
            arr[$j]=${arr[$j+1]}
            arr[$j+1]=$temp
        fi
    done
  done

  echo "${arr[@]}"
}

sample=(12 5 3 34 122 0 8 2 9 1 3 2 5 7 120)
echo "Unsorted: ${sample[@]}"
sorted=($(bubble_sort sample))
echo "Sorted: ${sorted[@]}"

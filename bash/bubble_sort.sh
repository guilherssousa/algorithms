#!/bin/bash

bubble_sort() {
  for i in $1; do
    for j in $(($1-$i-1)); do
      if [ $j -gt $j+1 ]; then
      swap $j $j+1
      fi
    done
  done
}

sample=(12 5 3 34 122 0 8 2 9 1 3 2 5 7 120)
echo "Unsorted: ${sample[@]}"
echo "Sorted: $(bubble_sort ${sample[@]})"

import { generate_sample_array } from "./utils.js";

function qs(list, lo, hi) {
  if (lo >= hi) {
    return;
  }

  const partitionIndex = partition(list, lo, hi);

  qs(list, lo, partitionIndex - 1);
  qs(list, partitionIndex + 1, hi);
}

function partition(list, lo, hi) {
  const pivot = list[hi];

  let index = lo - 1;

  for (let i = lo; i < hi; i++) {
    if (list[i] <= pivot) {
      index++;
      const tmp = list[i];
      list[i] = list[index];
      list[index] = tmp;
    }
  }

  index++;
  list[hi] = list[index];
  list[index] = pivot;

  return index;
}

function quick_sort(list) {
  qs(list, 0, list.length - 1);
}

const sample_array = generate_sample_array(process.argv[2] || 200);
console.time("sort");
quick_sort(sample_array);
console.timeEnd("sort");

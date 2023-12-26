import { generate_sample_array } from "./utils.js";

export default function bubble_sort(arr) {
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr.length - 1 - i; j++) {
      if (arr[j] > arr[j + 1]) {
        const tmp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = tmp;
      }
    }
  }
}

const sample = generate_sample_array(process.argv[2] || 30);
console.time("sort");
bubble_sort(sample);
console.timeEnd("sort");

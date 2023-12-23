function generate_sample_array(size = 30) {
  return Array.from({ length: size }).map(() =>
    Math.floor(Math.random() * 100),
  );
}

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

const sample = generate_sample_array();
console.log("Before sort:", sample);
bubble_sort(sample);
console.log("After sort:", sample);

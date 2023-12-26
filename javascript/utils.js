export function generate_sample_array(size = 30) {
  return Array.from({ length: size }).map(() =>
    Math.floor(Math.random() * 100),
  );
}

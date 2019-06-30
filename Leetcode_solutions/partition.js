module.exports = function partition(A, low, high) {
  pivot = A[high];

  index = low - 1;
  for (let j = low; j < high; j++) {
    if (A[j] <= pivot) {
      index += 1;
      temp = A[index];
      A[index] = A[j];
      A[j] = temp;
    }
  }
  temp1 = A[index + 1];
  A[index + 1] = A[high];
  A[high] = temp1;
  return index + 1;
};

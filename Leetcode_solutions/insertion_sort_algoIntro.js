function insertionSort(A) {
  for (let j = 2; j < A.length; j++) {
    key = A[j];
    i = j - 1;
    while (i > 0 && A[i] > key) {
      A[i + 1] = A[i];
      i -= 1;
    }
    A[i + 1] = key;
  }
  return A;
}

console.log(insertionSort([1, 9, 432, 90, 25, 62]));

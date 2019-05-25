function selectionSort(A, N) {
  for (let i = 0; i < N; i++) {
    minj = i;
    for (let j = i; j < N; j++) {
      if (A[j] < A[minj]) {
        minj = j;
      }
    }
    sw = A[i];
    A[i] = A[minj];
    A[minj] = sw;
  }
  return A;
}

console.log(selectionSort([3, 1, 4, 5, 2, 4, 0], 7));

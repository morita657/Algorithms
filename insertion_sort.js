function insertionSort(A, N) {
  for (let i = 0; i < N; i++) {
    let v = A[i];
    j = i - 1;
    while (j >= 0 && A[j] > v) {
      A[j + 1] = A[j];
      j--;
    }
    A[j + 1] = v;
  }
  return A;
}

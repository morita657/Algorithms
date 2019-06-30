function insertion(A, N) {
  for (let i = 0; i < N; i++) {
    v = A[i];
    j = i - 1;
    while (j >= 0 && A[j] > v) {
      A[j + 1] = A[j];
      j--;
    }
    A[j + 1] = v;
  }
  return A;
}
insertion([5, 3, 2, 1], 4);
console.log(insertion([5, 3, 2, 1], 4));

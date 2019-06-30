function bubbleSort(A, N) {
  flag = 1;
  while (flag) {
    flag = 0;
    for (let j = N - 1; j > 0; j--) {
      if (A[j] < A[j - 1]) {
        sw = A[j];
        A[j] = A[j - 1];
        A[j - 1] = sw;
        flag = 1;
      }
    }
  }
  return A;
}

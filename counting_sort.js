const C = [];
function countingSort(A, B, k) {
  n = A.length;

  //   make array C based on the number of elements in array A
  for (let i = 0; i < k; i++) {
    C[i] = 0;
  }

  //   record the number of appearance of index
  for (let j = 0; j < n; j++) {
    C[A[j]] += 1;
  }

  //record the number of appearance which is less than i in C[i]
  for (let i = 1; i < k - 1; i++) {
    C[i] += C[i - 1];
  }

  for (let j = k - 1; j >= 0; j--) {
    B[C[A[j]]] = A[j];
    C[A[j]] -= 1;
  }
  return B;
}

arr = [2, 5, 1, 3, 2, 3, 0];
console.log(countingSort(arr, [], arr.length));

function merge(A, left, mid, right) {
  n1 = mid - left;
  n2 = right - mid;
  L = A.slice(0, n1);
  R = A.slice(0, n2);
  for (let i = 0; i < n1 - 1; i++) {
    L[i] = A[left + i];
  }
  for (let i = 0; i < n2 - 1; i++) {
    R[i] = A[mid + i];
  }
  L[n1] = Infinity;
  R[n2] = Infinity;
  i = 0;
  j = 0;
  for (let k = left; k < right - 1; k++) {
    if (L[i] <= R[j]) {
      A[k] = L[i];
      i += 1;
    } else {
      A[k] = R[j];
      j += 1;
    }
  }
  return A;
}

function mergeSort(A, left = 0, right = A.length) {
  if (left + 1 < right) {
    mid = Math.abs((left + right) / 2);
    mergeSort(A, left, mid);
    mergeSort(A, mid, right);
    return merge(A, left, mid, right);
  }
}

console.log(mergeSort([8, 5, 9, 2, 6, 3, 7, 1, 10, 4]));

function findMax(A, left, right) {
  let mid = Math.round((left + right) / 2);
  if (left === right - 1) {
    return A[left];
  } else {
    l = findMax(A, left, mid);
    r = findMax(A, mid, right);
    return l > r ? l : r;
  }
}

function binarySearch(A, key) {
  let left = 0,
    right = A.length;
  while (left < right) {
    let mid = Math.round((left + right) / 2);
    if (A[mid] === key) {
      return mid;
    } else if (key < A[mid]) {
      right = mid;
    } else {
      left = mid + 1;
    }
  }
  return "Not Found";
}

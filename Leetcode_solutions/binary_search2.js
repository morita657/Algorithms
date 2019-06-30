function binarySearch(A, b) {
  n = A.length;

  if (n === 0) {
    return false;
  } else if (A[n / 2] === b) {
    return true;
  } else if (A[n / 2] > b) {
    return binarySearch(A.slice(0, n / 2), b);
  } else {
    return binarySearch(A.slice(n / 2, n - 1), b);
  }
}
console.log(binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6));

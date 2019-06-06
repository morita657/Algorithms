function partition(A, p, r) {
  x = A[r];
  i = p - 1;
  for (let j = p; j < r - 1; j++) {
    if (A[j] <= x) {
      i += 1;
      temp = A[i];
      A[i] = A[j];
      A[j] = temp;
    }
  }
  temp1 = A[i + 1];
  A[i + 1] = A[r];
  A[r] = temp1;
  i += 1;
  return i;
}
function main() {
  let i = 0,
    q,
    n = N.length;
  q = partition(N, 0, n);
  for (i = 0; i < n; i++) {
    console.log(i, q);

    if (i) {
      console.log(" ");
    }
    if (i === q) {
      console.log("[");
    }
    console.log(N[i]);
    if (i === q) {
      console.log("]");
    }
  }
  return 0;
}

N = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11];
main();

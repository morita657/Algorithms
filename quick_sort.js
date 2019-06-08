const partitionModule = require("./partition");

function quickSort(A, p, r) {
  if (p < r) {
    q = partitionModule(A, p, r);
    quickSort(A, p, q - 1);
    quickSort(A, q + 1, r);
  }
  return A;
}

N = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11];
console.log(quickSort(N, 0, N.length - 1));

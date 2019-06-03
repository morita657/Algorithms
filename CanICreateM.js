function solve(i, m) {
  if (m === 0) {
    return true;
  }
  if (i >= n) {
    return false;
  }
  res = solve(i + 1, m) || solve(i + 1, m - A[i]);
  return res;
}

A = [1, 5, 7];
m = 7;
n = A.length;
console.log(solve(A[0], m));

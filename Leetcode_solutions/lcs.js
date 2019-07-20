N = 1000;
function lcs(X, Y) {
  // make 2-d array
  c = [];
  for (let i = 0; i <= N; i++) {
    c.push([]);
  }
  maxl = 0;
  cnt = 0;

  m = X.length;
  n = Y.length;
  for (let i = 1; i <= m; i++) {
    c[i][0] = 0;
  }
  for (let j = 1; j <= n; j++) {
    c[0][j] = 0;
  }
  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      if (X[i] === Y[j]) {
        c[i][j] = c[i - 1][j - 1] + 1;
        cnt++;
      } else if (c[i - 1][j] >= c[i][j - 1]) {
        c[i][j] = c[i - 1][j];
        cnt++;
      } else {
        c[i][j] = c[i][j - 1];
        cnt++;
      }
      maxl = Math.max(maxl, c[i][j]);
    }
  }

  return cnt;
}

console.log(lcs("abcbdab", "bdcaba"));
console.log(lcs("sea", "eat"));

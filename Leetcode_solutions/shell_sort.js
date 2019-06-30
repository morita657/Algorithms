function insertionSort(A, n, g) {
  for (let i = g; i < n; i++) {
    v = A[i];
    j = i - g;
    while (j >= 0 && A[j] > v) {
      A[j + g] = A[j];
      j = j - g;
    }
    A[j + g] = v;
  }
  return A;
}

function shellSort(A, n) {
  // start form big g;
  m = n; // sorting range depends on m.
  G = [1, 4, 13, 40, 121, 364];
  for (let h = 1; ; ) {
    if (h > n) break;
    G.push(h);
    h = 3 * h + 1;
  }
  for (let i = G.length - 1; i >= 0; i--) {
    insertionSort(A, n, G[i]);
  }
  return A;
}

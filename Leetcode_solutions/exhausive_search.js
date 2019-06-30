function makeCombination() {
  for (let i = 0; i < n - 1; i++) {
    S[i] = 0;
  }
  rec(0);
}

function rec(i) {
  if (i === n) {
    console.log(S);
    return;
  }
  rec(i + 1);
  S[i] = 1;
  rec(i + 1);
  S[i] = 0;
}

S = [1, 2, 3, 4, 5, 6];
n = 5;
console.log(makeCombination());

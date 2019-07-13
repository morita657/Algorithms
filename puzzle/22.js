n = 16;
pair = [];
for (let i = 0; i < n / 2 + 1; i++) {
  pair.push("");
}
pair[0] = 1;

for (let i = 1; i < n / 2 + 1; i++) {
  pair[i] = 0;
  for (let j = 0; j < i; j++) {
    pair[i] += pair[j] * pair[i - j - 1];
  }
}
console.log(pair[n / 2]);

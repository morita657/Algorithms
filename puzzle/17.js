function main() {
  const b = "B",
    g = "G",
    N = 4;
  cnt = 0;
  function add(seq) {
    // console.log(seq);
    if (seq.length === N) {
      return 1;
    } else {
      cnt += add(seq + b);
      if (seq[-1] === b) {
        cnt += add(seq + g);
      }
    }
    return cnt;
  }
  return add(b) + add(g);
}

console.log(main());

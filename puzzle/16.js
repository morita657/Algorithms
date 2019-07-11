function main() {
  MAX = 400;
  let c = 1; //one side of square
  answer = [];
  candidates = [];
  count = 0;
  for (c; c < MAX / 4; c++) {
    let tate = 1;
    for (tate; tate <= c; tate++) {
      yoko = 2 * c - tate;
      combination = tate * yoko;
      if (combination == c * c) {
        count++;
      }
    }
  }
  return count;
}

console.log(main());

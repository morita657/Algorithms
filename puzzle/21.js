let count = 0,
  line = 1,
  row = [1];
function main(n) {
  let j = 0;
  let prevR = [];
  while (j <= n) {
    prevR = row;
    row = [];
    row.push(1);
    line++;
    for (let i = 1; i < prevR.length; i++) {
      if (
        (prevR[i - 1] === 1 && prevR[i] === 1) ||
        (prevR[i - 1] === 0 && prevR[i] === 0)
      ) {
        row.push(0);
        count++;
      } else {
        row.push(1);
      }
      if (n === count) {
        return { count, row, line };
      }
    }
    row.push(1);
    j++;
  }
}
console.log(main(1));
console.log(main(3));

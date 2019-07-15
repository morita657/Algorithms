/**
 * @param {number} N
 * @param {number} K
 * @return {number}
 */
var kthGrammar = function(N, K) {
  let line = "0",
    row = 1;
  while (row <= N) {
    temp = line;
    line = line.split("");
    for (let i = 0; i < temp.length; i++) {
      if (temp[i] === "0") {
        line[i] = "01";
      } else {
        line[i] = "10";
      }
    }
    line = line.join("");
    row++;
  }

  for (let j = 0; j < line.length; j++) {
    if (j === K - 1) {
      return line[j];
    }
  }
};

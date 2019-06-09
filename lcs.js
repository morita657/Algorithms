let main = (standardInput) => {
  let q = standardInput.split("\n"),
    num = Number.parseInt(q),
    i = 0;
  const input = [];

  while (i < num * 2) {
    input.push([q[i + 1], q[i + 2]]);
    (first = []), (second = []);
    i += 2;
  }

  const lcs = (X, Y, m, n) => {
    // base case n===0, m===0
    if (n === 0 || m === 0) {
      result = 0;
    } else if (X[m - 1] === Y[n - 1]) {
      result = 1 + lcs(X, Y, m - 1, n - 1);
    } else if (X[m - 1] !== Y[n - 1]) {
      tmp1 = lcs(X, Y, m - 1, n);
      tmp2 = lcs(X, Y, m, n - 1);
      result = Math.max.apply(null, [tmp1, tmp2]);
    }

    return result;
  };

  //   input each strings in lcs and return the length of longeest common string
  let j = 0;
  while (j < input.length) {
    console.log(
      lcs(input[j][0], input[j][1], input[j][0].length, input[j][1].length)
    );
    j++;
  }
};
main(require("fs").readFileSync("./dev/stdin/input.txt", "UTF-8"));

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
    const c = [];
    for (let i = 0; i < X.length; i++) {
      c.push([]);
      for (let j = 0; j < X.length; j++) {
        c[i].push(0);
      }
    }
    let temp1, temp2, temp3;
    for (let i = 0; i < X.length; i++) {
      for (let j = 0; j < Y.length; j++) {
        if (X[i] === Y[j]) {
          d = 1;
        } else {
          d = 0;
        }

        if (i > 0 && j > 0) {
          tmp1 = c[i - 1][j - 1] + d;
          // tmp2 = c[i - 1][j];
          // tmp3 = c[i][j - 1];
          console.log("tmp1, tmp2, tmp3: ", tmp1, tmp2, tmp3);
        } else if (i > 0) {
          tmp2 = c[i - 1][j];
        } else if (j > 0) {
          tmp3 = c[i][j - 1];
        }
        result = Math.max.apply(null, [tmp1, tmp2, tmp3]);
      }
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
main(require("fs").readFileSync("/dev/stdin", "UTF-8"));
main(require("fs").readFileSync("./../dev/stdin/input.txt", "UTF-8"));

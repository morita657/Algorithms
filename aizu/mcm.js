let main = (standardInput) => {
  let q = standardInput.split("\n"),
    num = Number.parseInt(q),
    i = 0;
  const input = [];

  while (i < num) {
    r = q[i + 1].split(" ")[0];
    c = q[i + 1].split(" ")[1];
    input.push([r, c]);
    i++;
  }

  n = input.length;
  m = input;
  p = [];
  const matrixChainMultiplication = () => {
    for (let i = 0; i < n; i++) {
      m[i][i] = 0;
      p[i - 1] = p[i];
    }

    for (let l = 2; l < n; l++) {
      for (let i = 1; i < n - l + 1; i++) {
        j = i + l - 1;
        m[i][j] = 0;
        for (let k = i; k < j - 1; k++) {
          m[i][j] = Math.min.apply(null, [
            m[i][j],
            m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
          ]);
        }
      }
    }
    console.log(m);
  };

  //   input each strings in lcs and return the length of longeest common string
  let j = 0;
  console.log(matrixChainMultiplication());
};

main(require("fs").readFileSync("./../dev/stdin/input.txt", "UTF-8"));

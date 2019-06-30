let main = (standardInput) => {
  let q = standardInput.split("\n"),
    num = Number.parseInt(q),
    i = 0;
  const input = [];

  while (i < num) {
    n = q[i + 1].split(" ")[0];
    u = q[i + 1].split(" ")[1];
    k = q[i + 1].split(" ")[2];
    v = q[i + 1].split(" ")[3];
    input.push([n, u, k, v]);
    i++;
  }
  //   console.log(input);

  const graph = (n, u, k, v) => {
    M = [];
    for (let i = 0; i < 100; i++) {
      for (let j = 0; j < 100; j++) {
        // console.log(M.push([]));
        M.push([]);
      }
    }
    // console.log(M);
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        // console.log(M.push([]));
        M[i][j] = 0;
      }
    }
    // console.log(M);

    for (let i = 0; i < n; i++) {
      u--;
      for (let j = 0; j < k; j++) {
        v--;
        M[u][v] = 1;
      }
    }

    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        M[i][j] = " ";
      }
    }
    return 0;
  };

  //   input each strings in lcs and return the length of longeest common string
  let j = 0;
  while (j < input.length) {
    // while (k < input[j].length) {
    console.log(graph(input[j][0], input[j][1], input[j][2], input[j][3]));
    // }
    j++;
  }
};
//   main(require("fs").readFileSync("/dev/stdin", "UTF-8"));
main(require("fs").readFileSync("./../dev/stdin/input.txt", "UTF-8"));

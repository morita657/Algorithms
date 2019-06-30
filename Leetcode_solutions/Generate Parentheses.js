/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
  const ans = [];
  generate(n, ans);
  return ans;
};

const generate = (n, ans, A = []) => {
  if (A.length === 2 * n) {
    if (valid(A)) {
      const str = A.reduce((total, crr) => total.concat(crr), "");
      ans.push(str);
    }
  } else {
    A.push("(");
    generate(n, ans, A);
    A.pop();
    A.push(")");
    generate(n, ans, A);
    A.pop();
  }
};
const valid = (A) => {
  let bal = 0;
  for (let c in A) {
    if (A[c] === "(") {
      bal += 1;
    } else {
      bal -= 1;
    }
    if (bal < 0) return false;
  }
  return bal === 0;
};

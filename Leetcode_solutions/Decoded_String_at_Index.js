/**
 * @param {string} S
 * @param {number} K
 * @return {string}
 */
var decodeAtIndex = function(S, K) {
  let tape = "";
  const chr = /[a-zA-Z]/g;
  const num = /[0-9]/g;
  for (let i = 0; i < S.length; i++) {
    if (S[i].match(chr)) {
      tape = tape.concat(S[i]);
      if (tape.length > K) {
        return tape.slice(K - 1, K);
      }
    }
    if (S[i].match(num)) {
      if (tape.length > K) {
        return tape.slice(K - 1, K);
      }
      tape += tape.repeat(S[i] - 1);
    }
  }
  return tape.slice(K - 1, K);
};

/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
  M = ["", "M", "MM", "MMM"];
  C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"];
  X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"];
  I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"];

  frth = M[Math.floor(num / 1000)] || "";
  t = C[Math.floor((num % 1000) / 100)] || "";
  s = X[Math.floor((num % 100) / 10)] || "";
  f = I[num % 10] || "";
  return frth + t + s + f;
};

/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function(a, b) {
  _a = a.length - 1;
  _b = b.length - 1;
  carry = 0;
  sum = [];
  digit = _a + _b + 2;
  while (_a >= 0 || _b >= 0) {
    current = parseInt(a[_a--] || 0) + parseInt(b[_b--] || 0) + carry;
    newDigit = current % 2;

    carry = Math.floor(current / 2);
    sum[digit--] = newDigit;
  }
  if (carry) {
    sum.splice(0, 0, carry);
  }
  return sum.join("");
};

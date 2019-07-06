function intToRoman(num) {
  var hash = [
    ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
    ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
    ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
    ["", "M", "MM", "MMM"]
  ];

  var result = "";
  var counter = 0;
  while (num > 0) {
    result = hash[counter++][num % 10] + result;
    num = Math.floor(num / 10);
  }

  return result;
}

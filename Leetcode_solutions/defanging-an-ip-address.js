/**
 * @param {string} address
 * @return {string}
 */
var defangIPaddr = function(address) {
  address = address.split(".");
  defIP = "";
  for (let i = 0; i < address.length - 1; i++) {
    defIP += address[i] + "[.]";
  }
  return defIP + address[address.length - 1];
};

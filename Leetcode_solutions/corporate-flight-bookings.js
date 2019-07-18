/**
 * @param {number[][]} bookings
 * @param {number} n
 * @return {number[]}
 */
var corpFlightBookings = function(bookings, n) {
  flights = {};
  for (let i = 1; i <= n; i++) {
    flights[i] = 0;
  }
  for (let i = 0; i < bookings.length; i++) {
    for (let j = bookings[i][0]; j <= bookings[i][1]; j++) {
      if (j in flights) {
        flights[j] += bookings[i][2];
      } else {
        flights[j] = bookings[i][2];
      }
    }
  }

  res = [];
  flNumber = Object.keys(flights);
  for (let i = 1; i <= n; i++) {
    if (i === parseInt(flNumber[i - 1])) {
      res.push(flights[i]);
    }
  }
  return res;
};

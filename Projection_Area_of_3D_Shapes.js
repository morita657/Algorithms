/**
 * @param {number[][]} grid
 * @return {number}
 */
var projectionArea = function(grid) {
  let top = 0,
    front = 0,
    side = 0;
  const frontPair = [];
  // TOP
  grid.forEach((elem) => {
    elem.forEach((val) => {
      if (val > 0) {
        top++;
      }
    });
  });
  // SIDE
  grid.forEach((elem) => {
    let current = 0;
    elem.forEach((val) => {
      if (current < val) {
        current = val;
      }
    });
    // console.log(current);
    side += current;
  });
  // FRONT
  grid.forEach((elem) => {
    elem.forEach((val, key) => {
      if (frontPair[key] === undefined) {
        frontPair[key] = val;
      } else if (val > frontPair[key]) {
        frontPair[key] = val;
      }
    });
  });
  front = frontPair.reduce((total, crr) => total + crr, 0);
  return top + side + front;
};

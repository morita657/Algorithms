/**
 * @param {number[]} piles
 * @return {boolean}
 */
var stoneGame = function(piles) {
  (alex = []), (lee = []);
  //   remove first element for alex
  first =
    piles[0] > piles[piles.length - 1] ? piles[0] : piles[piles.length - 1];
  alex.push(first);
  //   remove the taken element by alex from the piles
  piles.splice(piles.indexOf(first), 1);

  alTotal = alex.reduce((acc, crr) => acc + crr, 0);
  leTotal = lee.reduce((acc, crr) => acc + crr, 0);
  // start the game from lee
  const game = (piles, alex, lee) => {
    //     base
    if (piles.length === 0) {
      console.log(alex, lee);
      return alTotal > leTotal;
    } else {
      //   find max elem
      curr = piles[0];
      for (let i = 0; i < piles.length; i++) {
        if (piles[i] > curr) {
          curr = piles[i];
        }
      }
      if (lee.length < alex.length) {
        lee.push(curr);
      } else {
        alex.push(curr);
      }
      piles.splice(piles.indexOf(curr), 1);
      game(piles, alex, lee);
    }
  };

  game(piles, alex, lee);
  return alTotal > leTotal;
};

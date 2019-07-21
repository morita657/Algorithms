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
      return alTotal > leTotal;
    } else {
      if (lee.length < alex.length) {
        lee.push(first);
      } else {
        alex.push(first);
      }
      piles.splice(piles.indexOf(first), 1);
      game(piles, alex, lee);
    }
  };

  game(piles, alex, lee);
  return alTotal > leTotal;
};

var fourSum = function(nums, target) {
  return kSum(nums, target, 4);
};

var kSum = function(nums, target, k) {
  let toSum = (ns, t, k, start) => {
    let res = [];
    if (k == 2) {
      // 2 sum; ( improved to O(n) )
      let rp = ns.length - 1;
      let lp = start;
      while (lp < rp) {
        if (ns[lp] + ns[rp] == t) {
          res.push([ns[lp], ns[rp]]);
          //skip duplication
          while (lp < rp && ns[lp] == ns[lp + 1]) lp++;
          while (lp < rp && ns[rp] == ns[rp - 1]) rp--;
          lp++;
          rp--;
        } else if (ns[lp] + ns[rp] < t) lp++;
        else rp--;
      }
    } else {
      for (let i = start; i < ns.length - k + 1; i++) {
        let temp = toSum(ns, t - ns[i], k - 1, i + 1);
        temp.forEach((t) => {
          t.push(ns[i]);
          res.push(t);
        });
        //skip duplication
        while (i < ns.length - 1 && ns[i] == ns[i + 1]) i++;
      }
    }
    return res;
  };

  nums = nums.sort((a, b) => a - b);
  return toSum(nums, target, k, 0);
};

var fourSum = function(nums, target) {
  return kSum(nums, target, 4);
};

var kSum = function(nums, target, k) {
  let toSum = (ns, t, k, start) => {
    let res = [];
    if (k == 1) {
      // recursive to only one target num ( the sum of last two num should be O(n^2))
      for (let i = start; i < ns.length; i++) {
        if (ns[i] == t) return [[ns[i]]];
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

function main(list) {
  let minv = list[0],
    maxv = -20000000;
  for (let j = 1; j < list.length; j++) {
    if (maxv > list[j] - minv) {
      maxv = maxv;
    } else {
      maxv = list[j] - minv;
    }
    if (minv < list[j]) {
      minv = minv;
    } else {
      minv = list[j];
    }
  }
  console.log(maxv, minv);

  return maxv - minv;
}
console.log(main([6, 5, 3, 1, 3, 4, 3]));
console.log(main([3, 4, 3, 2]));

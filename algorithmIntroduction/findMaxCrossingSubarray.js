function FMCS(A, low, mid, high) {
  let maxLeft, leftSum, maxRight, rightSum;
  leftSum = -100;
  sum = 0;
  for (let i = mid; i > low; i--) {
    sum += A[i];
    if (sum > leftSum) {
      leftSum = sum;
      maxLeft = i;
    }
  }
  rightSum = -100;
  sum = 0;
  for (let j = mid + 1; j < high; j++) {
    sum += A[j];
    if (sum > rightSum) {
      rightSum = sum;
      maxRight = j;
    }
  }

  return { maxLeft, maxRight, leftSum, rightSum };
}
Arr = [1, 7, 3, 7, 9, 543, 654, 3, 65, 4, 24];
len = Arr.length;
console.log(FMCS(Arr, 0, Math.round(len / 2), len));

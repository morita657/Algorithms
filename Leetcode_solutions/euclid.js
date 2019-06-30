function euclid(m, n) {
  while (m != n && m > 0 && n > 0) {
    r = m % n;
    if (r === 0) {
      return n;
    }
    m = n;
    n = r;
  }
}

console.log(euclid(1633, 355));

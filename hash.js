function h1(key) {
  return key % 7;
}

function h2(key) {
  return 1 + (key % 6);
}

function h(key, i) {
  return (h1(key) + i * h2(key)) % 6;
}

function insert(T, key) {
  let i = 0;
  while (true) {
    j = h(key, i);
    if (T[j] === null) {
      T[j] = key;
      return j;
    } else {
      i += 1;
    }
  }
}

function koch(d, p1, p2) {
  if (d === 0) {
    return;
  }

  let s, t, u;
  const th = (Math.PI * 60.0) / 180.0;
  s = {
    x: (2.0 * p1.x + 1.0 * p2.x) / 3.0,
    y: (2.0 * p1.x + 1.0 * p2.x) / 3.0
  };
  t = {
    x: (1.0 * p1.x + 2.0 * p2.x) / 3.0,
    y: (1.0 * p1.x + 2.0 * p2.x) / 3.0
  };
  u = {
    x: (t.x - s.x) * Math.cos(th) + (t.y - s.y) * Math.sin(th) + s.x,
    y: (t.x - s.x) * Math.sin(th) + (t.y - s.y) * Math.cos(th) + s.y
  };

  // p1, p2からs, u, tの座標を計算
  koch(d - 1, p1, s);
  console.log(s.x, s.y);
  koch(d - 1, s, u);
  console.log(u.x, u.y);
  koch(d - 1, u, t);
  console.log(t);
  koch(d - 1, t, p2);
}
function main() {
  let a,
    b,
    n = 1;
  a = {
    x: 0,
    y: 0
  };
  b = {
    x: 100,
    y: 0
  };
  console.log(a);
  koch(n, a, b);
  console.log(b);
  return 0;
}
console.log(main());

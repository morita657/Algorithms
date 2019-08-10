class BinaryHeap {
  constructor() {
    this.heap = [30, 20, 10, 7, 9, 5];
    this.sz = 0;
  }

  insert(val) {
    this.heap.push(val);
    this.bubbleUp();
  }

  bubbleUp() {
    //   targte index
    let i = this.sz++;
    while (i > 0) {
      // parent index
      let p = (i - 1) / 2;
      if (this.heap[p] <= x) break;
      this.heap[i] = this.heap[p];
      i = p;
    }
    heap[i] = x;
  }

  pop() {
    //   minimum value
    let ret = this.heap[0];
    // value to bring to the root
    let x = this.heap[this.sz--];
    // bubble down from the root
    let i = 0;
    while (i * 2 + 1 < this.sz) {
      // compare between children
      let a = i * 2 + 1,
        b = i * 2 + 2;
      if (b < this.sz && this.heap[b] < this.heap[a]) {
        a = b;
      }
      // break when there is no upsidedown
      if (this.heap[a] >= x) {
        break;
      }
      //   hoist the children's value
      heap[i] = heap[a];
    }
    heap[i] = x;
    return ret;
  }
}

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
    head = this.heap[0];
    this.heap[0] = this.heap.pop();
    this.bubbleDown(0);
    return head;
  }

  bubbleDown(index) {
    let left = index * 2 + 1,
      right = index * 2 + 2,
      largest = index;
    // if left node is larger than , swap it
    if (this.heap[left] > this.heap[largest]) {
      largest = left;
    }
    //   if right node is larger than the head, swap it
    if (this.heap[right] > this.heap[largest]) {
      largest = right;
    }
    // swap
    if (index !== largest) {
      temp = largest;
      largest = index;
      index = temp;
      [this.heap[index], this.heap[largest]] = [
        this.heap[largest],
        this.heap[index]
      ];
      this.bubbleDown(largest);
    }
  }
}

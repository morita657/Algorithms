class Heap {
  constructor(heap) {
    this.heap = [];
    this.heap.data = {};
  }

  insert(heap) {
    //   add element in the end of heap
    heap.push();
    heap.data[heap.length - 1];

    let i = heap.length - 1;
    while (i > 0) {
      if (heap.data[(i - 1) / 2] > heap.data[i]) {
        sw = heap.data[i];
        heap.data[i] = heap.data[(i - 1) / 2];
        heap.data[(i - 1) / 2] = sw;
      } else {
        return;
      }
    }
  }

  deletemin(heap) {
    object = heap.data[0];
    heap.data[0] = heap.data[heap.length - 1];
    heap.data[heap.length - 1] = heap.data[heap.length - 2];

    i = 0;
    while (i < heap.data[heap.length - 1 / 2]) {
      if (heap.data[i] > heap.data[i * 2 + 1]) {
        if (heap.data[i * 2 + 2] < heap.data[i * 2 + 1]) {
          sw = heap.data[i];
          heap.data[i] = heap.data[i * 2 + 2];
          heap.data[i * 2 + 2] = sw;
          i = i * 2 + 2;
        } else {
          sw = heap.data[i];
          heap.data[i] = heap.data[i * 2 + 1];
          heap.data[i * 2 + 1] = sw;
          i = i * 2 + 1;
        }
      } else if (heap.data[i] > heap.data[i * 2 + 2]) {
        sw = heap.data[i];
        heap.data[i] = heap.data[i * 2 + 2];
        heap.data[i * 2 + 2] = sw;
        i = i * 2 + 1;
      } else {
        return object;
      }
    }
  }
}

h = new Heap();
h.insert(31);
h.insert(21);
h.insert(48);
h.insert(9);
console.log(h.data);

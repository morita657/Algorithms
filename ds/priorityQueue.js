class Node {
  constructor(val, priority) {
    this.val = val;
    this.priority = priority;
    this.next = null;
  }
}

class PriorityQueue {
  constructor(val) {
    this.root = new Node(val);
  }
  add(val, priority) {
    const newNode = Node(val, priority);
    if (!this.root && priority > this.root.priority) {
      newNode.next = this.root;
      this.root = newNode;
    } else {
      let pointer = this.root;
      while (pointer.ext && priority < pointer.next.priority) {
        pointer = pointer.next;
      }
      pointer.next = newNode;
    }
  }
  remove(val) {
    let first = this.root;
    first = first.next;
    return first;
  }
}

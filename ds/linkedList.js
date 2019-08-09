class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

// n = new Node(2);
// n.next = new Node(3);
// console.log(n);

class LinkedList {
  constructor(val) {
    this.head = new Node(val);
  }
  add(val) {
    if (this.head === null) {
      this.head = new Node(val);
    } else {
      const newNode = new Node(val);
      let current = this.head;
      while (current.next !== null) {
        current = current.next;
      }
      current.next = newNode;
    }
    return this.head;
  }
  search(target) {
    let current = this.head;
    while (current) {
      if (current.val == target) {
        return true;
      }
      current = current.next;
    }
    return false;
  }
  delete(target) {
    let current = this.head;
    if (current.val == target) {
      current = current.next;
    } else {
      while (current) {
        if (current.val === target) {
          //   current.val = current.next.val;
          current = current.next;
        }
        current = current.next;
      }
      return this.head;
    }
  }
}
list = new LinkedList(5);
console.log(list.add(3));
console.log(list.add(10));
console.log(list.search(3));
console.log(list.delete(3));

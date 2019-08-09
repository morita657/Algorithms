class Node {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

// node = new Node(3);
// node.left = new Node(5);
// node.right = new Node(10);

// console.log(node);

class BinarySeach {
  constructor(val) {
    this.root = new Node(val);
  }
  add(val, root = this.root) {
    let current = root;
    if (val > current.val) {
      if (current.right == null) {
        current.right = new Node(val);
      } else {
        this.add(val, current.right);
      }
    }

    if (val < current.val) {
      if (current.left == null) {
        current.left = new Node(val);
      } else {
        this.add(val, current.left);
      }
    }
    return this.root;
  }
  search(val, root = this.root) {
    if (root.val == val) {
      return true;
    } else if (val > root.val && root.right !== null) {
      this.search(val, root.right);
    } else if (val < root.val && root.left !== null) {
      this.search(val, root.left);
    } else {
      return false;
    }
    return false;
  }
}
bs = new BinarySeach(5);
console.log(bs.add(10));
console.log(bs.search(10));

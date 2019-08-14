class HashTable {
  constructor() {
    this.storage = {};
  }
  //   Best case O(1)
  //   Worst case O(n)
  add(target) {
    const hash = target.hashCode();
    const limit = 100;
    const key = hash % limit;
    if (!this.storage[key]) {
      this.storage[key] = [target];
    } else {
      this.storage[key].push(target);
    }
    return this.storage;
  }
  //   Best case O(1)
  //   Worst case O(n)
  search(target) {
    const hash = target.hashCode();
    const limit = 100;
    const key = hash % limit;
    if (Object.keys(this.storage).includes(key.toString())) {
      for (let i = 0; i < this.storage[key].length; i++) {
        if (target === this.storage[key][i]) {
          return true;
        }
      }
    } else {
      return false;
    }
  }
}

String.prototype.hashCode = function() {
  var hash = 0,
    i,
    chr;
  if (this.length === 0) return hash;
  for (i = 0; i < this.length; i++) {
    chr = this.charCodeAt(i);
    hash = (hash << 5) - hash + chr;
    hash |= 0; // Convert to 32bit integer
  }
  return hash;
};

hashtable = new HashTable();
console.log(hashtable);
console.log(hashtable.add("ally"));
console.log(hashtable.add("bill"));
console.log(hashtable.add("yossi"));
console.log(hashtable.search("yossi"));

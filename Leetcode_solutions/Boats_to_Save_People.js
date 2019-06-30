/**
 * @param {number[]} people
 * @param {number} limit
 * @return {number}
 */
var numRescueBoats = function(people, limit) {
  output = 0;
  people = people.sort((first, second) => second - first);
  for (let i = 0; i < people.length; i++) {
    if (people[i] === limit) {
      output++;
      people.splice(i, 1);
    }
  }
  const len = people.length;
  let front = 0,
    back = len - 1;
  while (people.length > 0) {
    if (people[front] + people[back] > limit) {
      output++;
      people.shift();
      back = people.length - 1;
    } else if (people[front] + people[back] <= limit) {
      output++;
      people.splice(back, 1);
      people.splice(front, 1);
      back = people.length - 1;
    } else {
      output++;
      people.shift();
    }
    people = people;
  }
  return output;
};

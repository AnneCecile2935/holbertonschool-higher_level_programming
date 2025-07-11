#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

const x = myObject;
x.value = 89;

console.log(myObject);

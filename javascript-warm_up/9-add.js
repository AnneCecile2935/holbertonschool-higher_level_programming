#!/usr/bin/node
const num1 = Number(process.argv[2]);
const num2 = Number(process.argv[3]);

function add (num1, num2) {
  return num1 + num2;
}
const x = add(num1, num2);
console.log(x);

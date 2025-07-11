#!/usr/bin/node
const args = Number(process.argv[2]);
const text = 'C is fun';
if (isNaN(args)) {
  console.log('Missing number of occurrences');
} else if (args >= 0) {
  for (let i = 0; i < args; i++) {
    console.log(text);
  }
}

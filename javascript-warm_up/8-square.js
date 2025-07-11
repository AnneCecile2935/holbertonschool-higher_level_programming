#!/usr/bin/node

const size = Number(process.argv[2]);
const text = 'X';
if (Number.isInteger(size) && size > 0) {
  for (let i = 0; i < size; i++) {
    console.log(text.repeat(size));
  }
} else {
  console.log('Missing size');
}

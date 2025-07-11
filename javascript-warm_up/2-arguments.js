#!/usr/bin/node
const args = process.argv;
if (args.length === 2) {
	console.log("argc[0]");
} else if (args.length === 3) {
	console.log("argc[1]");
} else {
	console.log("Arguments found");
}

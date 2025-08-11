"use string";

process.stdin.resume();
process.stdin.setEncoding("utf8");

let inputString: string = "";
let inputLines: string[] = [];
let currentLine: number = 0;

process.stdin.on("data", function (inputStdin: string): void {
  inputString += inputStdin;
});

process.stdin.on("end", function (): void {
  inputLines = inputString.split("\n");
  inputString = "";

  main();
});

function readLine(): string {
  return inputLines[currentLine++];
}

function staircase(n: number): void {
  for (let i: number = 1; i <= n; i++) {
    let space: string = " ".repeat(n - i);
    let hashes: string = "#".repeat(i);
    console.log(space.concat(hashes));
  }
}

function main(): void {
  const n: number = parseInt(readLine().trim(), 10);

  staircase(n);
}

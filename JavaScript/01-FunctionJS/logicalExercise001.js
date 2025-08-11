"user strict";

const fs = require("fs");

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = "";

process.stdin.on("data", function (inputStind) {
  inputString += inputStind;
});

process.stdin.on("end", function () {
  inputString = inputString.split("\n");
  main();
  readFileResults();
});

function readLine() {
  return inputString[currentLine++];
}

// 1. Encontrar al elemento con mas valor
// 2. Ver cuantas veces se repite el elemento mas valioso

function brithdayCakeCandles(candles) {
  let maxv = 0;
  let count = 0;
  for (let i = 0; i < candles.length; i++) {
    if (candles[i] > maxv) {
      maxv = candles[i];
    }
  }
  for (let i = 0; i < candles.length; i++) {
    if (candles[i] === maxv) {
      count++;
    }
  }
  return count;
}

function main() {
  const ws = fs.createWriteStream("./results.txt");

  const candlesCount = parseInt(readLine().trim(), 10);

  const candles = readLine()
    .replace(/\s+$/g, "")
    .split(" ")
    .map((candlesTemp) => parseInt(candlesTemp, 10));

  const result = brithdayCakeCandles(candles);

  ws.write(result + "\n");

  ws.end();
}

function readFileResults() {
  setTimeout(() => {
    fs.readFile("./results.txt", "utf8", (err, data) => {
      if (err) {
        console.log("[!] Hubo un error al leer el archivo", err);
        return;
      }

      console.log(data);
    });
  }, 100);
}

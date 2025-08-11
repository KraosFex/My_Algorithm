"use strict";

const fs = require("fs");

process.stdin.resume();
process.stdin.setEncoding("utf8");

let inputString = "";
let currentLine = 0;

process.stdin.on("data", function (inputStdin) {
  inputString += inputStdin;
});

process.stdin.on("end", function () {
  inputString = inputString.split("\n");
  main();
  readFileWithResults();
});

function readLine() {
  return inputString[currentLine++];
}

function readFileWithResults() {
  setTimeout(() => {
    fs.readFile("./results.txt", "utf8", (err, data) => {
      if (err) {
        console.log("[!] Ha ocurrido un erro al leer el archivo destino", err);
        return;
      }
      console.log(data);
    });
  }, 100);
}

function timeConversion(s) {
  let meridiem = s.split("").slice(8).join("");
  let hour = Number(s.split("").slice(0, 2).join(""));
  if (meridiem === "PM") {
    let militarHour = hour < 12 ? hora + 12 : 12;
    return militarHour + s.split("").slice(2, 8).join("");
  }
  if (hour === 12) return "00" + s.split("").slice(2, 8).join("");
  return s.split("").slice(0, 8).join("");
}

function main() {
  const ws = fs.createWriteStream("./results.txt");
  const s = readLine();
  const result = timeConversion(s);
  ws.write(result + "\n");
  ws.end();
}

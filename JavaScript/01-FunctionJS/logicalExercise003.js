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
        console.log("[!] Ocurruio un error inesperado al leer el archivo.");
        return;
      }

      console.log(data);
    });
  }, 100);
}

function gradingStudents(grades) {
  let results = [];
  for (let i = 0; i < grades.length; i++) {
    if (grades[i] < 38) {
      results.push(grades[i]);
      continue;
    }
    let x = grades[i] - (grades[i] % 5) + 5;
    if (x - grades[i] < 3) {
      results.push(x);
      continue;
    }
    results.push(grades[i]);
  }
  return results;
}

function main() {
  const ws = fs.createWriteStream("./results.txt");
  const gradeCount = parseInt(readLine().trim(), 10);

  let grades = [];

  for (let i = 0; i < gradeCount; i++) {
    const gradesItem = parseInt(readLine().trim(), 10);
    grades.push(gradesItem);
  }
  const results = gradingStudents(grades);

  ws.write(results.join("\n") + "\n");

  ws.end();
}

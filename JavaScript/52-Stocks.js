let stocksArr = [], largestDiffs = [];
for(let i = 0; i < 10; i++) { stocksArr.push(Math.round(Math.random() * 1000),) }
console.log(stocksArr)
for(let i = 0; i < 9; i++) {
  largestDiffs.push(stocksArr[i] - Math.min(...stocksArr.slice(i + 1, 10)));
}
console.log(`${(largestDiffs.indexOf(Math.max(...largestDiffs)))} ${stocksArr.indexOf(Math.min(...stocksArr.slice(largestDiffs.indexOf(Math.max(...largestDiffs)), 9)))}`);
const wordToBin = (word) => {
  wordArr = word.split("").map( (letter) => {
    return letter.charCodeAt(0);
  });
  return wordArr
}

const denToHex = (numIn) => {
  const hexDict = `0123456789abcdef`.split("");
  let rawHexArr = [], hexLength = 0, remainder = numIn;
  while (Math.pow(16, hexLength) < numIn) {
    hexLength += 1;
  }
  for(let i = 0; i <= hexLength; i++) {
    rawHexArr.push(0);
  }
  for(let i = hexLength; i >= 0; i--) {
    while(Math.pow(16, i) <= remainder) {
      rawHexArr[hexLength - i] += 1;
      remainder -= Math.pow(16, i);
    }
  }
  rawHexArr = rawHexArr.map( (denNum) => hexDict[denNum]);
  return rawHexArr.join("");
}

const wordToHex = (word) => {
  let numArrIn = wordToBin(word)
  let outArr = numArrIn.map( (num) => denToHex(num) );
  return outArr.join(",")
}

console.log(wordToHex("hello"))
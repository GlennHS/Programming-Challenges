const encryptVignere = (plain, keyword) => {
  alphabetArray = 'abcdefghijklmnopqrstuvwxyz'.split('');
  plain = plain.toLowerCase();
  keyword = keyword.toLowerCase();
  let keywordNums = [];
  keyword.split("").forEach( (letter) => {
    keywordNums.push(alphabetArray.indexOf(letter));
  });
  let plainNums = [];
  plain.split("").forEach( (letter) => {
    plainNums.push(alphabetArray.indexOf(letter));
  });
  let cipherNums = [];
  for (let i = 0; i < plainNums.length; i++) {
    ciphNum = ((plainNums[i] + keywordNums[i % keyword.length]) > 25 ? (plainNums[i] + keywordNums[i % keyword.length] - 25) : (plainNums[i] + keywordNums[i % keyword.length]));
    cipherNums.push(ciphNum);
  }
  let cipherArr = [];
  cipherNums.forEach( (num) => {
    cipherArr.push(alphabetArray[num])
  });
  return cipherArr.join("");
}

const decryptVignere = (cipher, keyword) => {
  alphabetArray = 'abcdefghijklmnopqrstuvwxyz'.split('');
  cipher = cipher.toLowerCase();
  keyword = keyword.toLowerCase();
  let keywordNums = [];
  keyword.split("").forEach( (letter) => {
    keywordNums.push(alphabetArray.indexOf(letter));
  });
  let cipherNums = [];
  cipher.split("").forEach( (letter) => {
    cipherNums.push(alphabetArray.indexOf(letter));
  });
  let plainNums = [];
  for (let i = 0; i < cipherNums.length; i++) {
    plaNum = ((cipherNums[i] - keywordNums[i % keyword.length]) < 0 ? (cipherNums[i] - keywordNums[i % keyword.length] + 25) : (cipherNums[i] - keywordNums[i % keyword.length]));
    plainNums.push(plaNum);
  }
  let plainArr = [];
  plainNums.forEach( (num) => {
    plainArr.push(alphabetArray[num])
  });

  return plainArr.join("");
}
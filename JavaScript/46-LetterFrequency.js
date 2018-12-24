'use strict'

const alphArr = 'abcdefghijklmnopqrstuvwxyz'.split("");

const getFreq = (words) => {
  const freqArr = [];
  let str = words.toLowerCase();
  alphArr.forEach( (letter) => {
    const re = new RegExp(`${letter}`, "g");
    freqArr.push(((str || '').match(re) || []).length);
    });
  return(freqArr)
}

const prettify = (frequencies) => {
  let pretty = [];
  for (let i = 0; i < alphArr.length; i++) {
    pretty.push([alphArr[i], frequencies[i]]);
  }
  return pretty;
}

const main = () => {
  console.log(prettify(getFreq(prompt("Input a phrase"))));
}
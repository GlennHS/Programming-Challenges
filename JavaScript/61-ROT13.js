let alphabet = "abcdefghijklmnopqrstuvwxyz".split("");

const encryptROT = (plain) => plain.split("").map( (letter) => alphabet.indexOf(letter) + 13).map( (cipheredNum) => alphabet[cipheredNum]).join("");  
const decryptROT = (cipher) => cipher.split("").map( (letter) => alphabet.indexOf(letter) - 13).map( (plainNum) => alphabet[plainNum]).join("");
console.log(encryptROT("hello"));
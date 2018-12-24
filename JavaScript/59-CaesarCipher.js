let alphabet = "abcdefghijklmnopqrstuvwxyz".split("");

const encryptCaesar = (plain, shift) => plain.split("").map( (letter) => alphabet.indexOf(letter) + shift).map( (cipheredNum) => alphabet[cipheredNum]).join("");  
const decryptCaesar = (cipher, shift) => cipher.split("").map( (letter) => alphabet.indexOf(letter) - shift).map( (plainNum) => alphabet[plainNum]).join("");
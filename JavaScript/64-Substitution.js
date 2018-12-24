const alphabet = "abcdefghijklmnopqrstuvwxyz".split("");

const encrypt = (newAlphArr = "bcdefghijklmnopqrstuvwxyza".split(""), plaintext = "thequickbrownfoxjumpedoverthelazydog".split("")) => {
  // Initialise out arr
  let outArr = []
  plaintext.forEach( () => outArr.push("-"))
  alphabet.forEach( (alphLetter, alphIndex) => {
    plaintext.forEach( (plainLetter, letterIndex) => {
      if(plainLetter === alphLetter) { outArr[letterIndex] = newAlphArr[alphIndex] }
    })
  })
  return outArr.join("");
}

const decrypt = (encrAlphArr = "bcdefghijklmnopqrstuvwxyza".split(""), ciphertext = "uifrvjdlcspxogpykvnqfepwfsuifmbazeph".split("")) => {
  // Initialise out arr
  let outArr = []
  ciphertext.forEach( () => outArr.push("-"))
  encrAlphArr.forEach( (alphLetter, alphIndex) => {
    ciphertext.forEach( (ciphLetter, letterIndex) => {
      if(ciphLetter === alphLetter) { outArr[letterIndex] = alphabet[alphIndex] }
    })
  })
  return outArr.join("");
}

console.log(decrypt())
let i

const generatePass = (caps, nums, symbols, length) => {
  let possibleNums = []
  if(symbols && nums && caps) {
    for(i = 32; i < 127; i++) {
      possibleNums.push(i) 
    }
  } else {
    for( len = 0; len < length; len++) {
      for(i = 97; i < 123; i++) { possibleNums.push(i) }
      if(caps) { for(i = 65; i < 91; i++) { possibleNums.push(i) } }
      if(nums) { for(i = 48; i < 58; i++) { possibleNums.push(i) } }
      if(symbols) { 
        for(i = 33; i < 48; i++) { possibleNums.push(i) }
        for(i = 58; i < 65; i++) { possibleNums.push(i) }
        for(i = 91; i < 97; i++) { possibleNums.push(i) }
        for(i = 123; i < 127; i++) { possibleNums.push(i) }
      }
    }
  }
  let outNums = []
  for(i = 0; i < length; i++) {
    outNums.push(possibleNums[Math.floor(Math.random() * possibleNums.length)]);
  }
  return String.fromCharCode(...outNums)
}

console.log(generatePass(true, true, false, 8));
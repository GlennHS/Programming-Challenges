  let piApprox = 3
  for(let i = 2; i < 1000; i++) {
    let change = 4 / ((2 * i - 2) * (2 * i - 1) * (2 * i))
    if(i % 2 === 0) {
      piApprox += change
    } else {
      piApprox -= change
    }
    console.log(piApprox)
  }
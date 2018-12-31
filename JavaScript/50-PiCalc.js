'use strict'

// Gregory-Leibniz series
// Slow Convergence / High Readability
const gregLeib = (iterations) => {
  let piApprox = 1
  for(let i = 2; i < iterations; i++) {
    if(i % 2 === 0) {
      piApprox -= 1 / (2 * i - 1)
    } else {
      piApprox += 1 / (2 * i - 1)
    }
  }
  return piApprox * 4
}

// Nilakantha Series
// Fast(er) Convergence / Moderate Readability
const nilakantha = (iterations) => {
  let piApprox = 3
  for(let i = 2; i < iterations; i++) {
    let change = 4 / ((2 * i - 2) * (2 * i - 1) * (2 * i))
    if(i % 2 === 0) {
      piApprox += change
    } else {
      piApprox -= change
    }
  }
  return piApprox
}

console.log(`\nGregory-Leibniz Approximation: ${gregLeib(1000)}\nNilakantha Approximation:      ${nilakantha(1000)}\n`)
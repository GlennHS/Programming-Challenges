let a = [24], complete;

while(!complete) {
  complete = true
  a.forEach( (factor, index) => {
    if(factor > 3) {
      for(let i = 2; i <= (factor / 2); i++) {
        if(factor % i === 0 && complete) {
          a.push(i, factor / i);
          a[index] = -1;
          complete = false
        }
      }
    }
  })
}

console.log(a)
console.log(Math.max(...a))
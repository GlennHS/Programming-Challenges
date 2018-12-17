'use strict'

const numTowers = 3, numRings = 3
let towers = []

const init = () => {
  for(let i = 0; i < numTowers; i++) { towers.push([]) }
  for(let i = 0; i < numRings; i++) { towers[0].push(i) }
}

const moveRing = (fromTower, toTower) => {
  const moving = towers[fromTower].pop() || -1
  const comparator = towers[toTower].pop() || -1
  if(moving !== -1) {
    console.log(`${moving} ${comparator}`)
    if(moving > comparator) {
      console.log('moved')
      towers[toTower].push(moving)
    } else {
      towers[fromTower].push(moving)
    }
  }
}

init()
moveRing(1, 0)
console.log(towers);
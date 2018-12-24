const checkWin = (choice, against) => {
  switch(choice) {
    case("Rock"): switch(against) {
                    case("Rock"): return "draw"
                    case("Paper"): return "lose"
                    case("Scissors"): return "win"
                  }
    case("Paper"):switch(against) {
                    case("Rock"): return "win"
                    case("Paper"): return "draw"
                    case("Scissors"): return "lose"
                  }
    case("Scissors"): switch(against) {
                        case("Rock"): return "lose"
                        case("Paper"): return "win"
                        case("Scissors"): return "draw"
                      }
  }
}

console.log(checkWin("Paper", "Scissors"))
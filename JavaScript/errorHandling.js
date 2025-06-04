function canYouSpotTheProblem() {
    "use strict";
    for (counter=0; counter < 10; counter++) {
        console.log("Happy happy");        
    }
}

// canYouSpotTheProblem();

function test(label, body) {
    if (!body()) console.log(`Failed: ${label}`);
}

test("1+1=2", () => 1 + 1 == 2);

test("2+2=5", () => 2 +2 == 5);

function checkNumberPrompt(question) {
    let result = Number(prompt(question));
    if (Number.isNaN(reult)) return null;
    return result;
}

function askForDirection(direction) {
    let result = prompt(direction);

    if (result.toLowerCase() == "left") return "L";
    else if (result.toLowerCase() == "right") return "R";
    else throw new Error("Invalid direction:" + result);    
}

function look() {
    const direction = askForDirection("Which way, left or right?");
    if (direction ==  "L") return "A Zoo"
    else {
        return "Shopping Mall";
    }
}

// try {
//     console.log(look());
// } catch (error) {
//     console.log("Something went wrong:" + error);    
// }

const accouts = {
    "vikas": 100,
    "akash": 200,
    "saurabh": 300
}

function getAccount(name) {
    if (Object.hasOwn(accouts, name.toLowerCase())) return name.toLowerCase()
    throw new Error("Invalid account name")
}

function moneyTransfer(from, to, amount) {
    
    try {
        let first = getAccount(from)
        let second = getAccount(to)
        console.log(`first: ${first}, second: ${second}`);
        if (accouts[first] >= amount) {
            accouts[first] -= amount;
            accouts[second] += amount;                 
        }
    } catch (e) {
        console.error("Error: ", e.message);
        // console.log("Some error occured: ", e);
    } finally {
        console.log("Accounts: ", accouts);       
    }
}

console.log(moneyTransfer("vikas", "aakash", 100));


class MultiplicationUnitFailure extends Error {}

function primitiveMultiply(a, b) {
    const rand = Math.random()
    if (rand < 0.05) return a * b
    throw new MultiplicationUnitFailure("Machine couldn't multiply the numbers.");
}

function multiplyAnyhow(a, b) {
    for (;;) {
        try {
            return primitiveMultiply(a, b)
        } catch(e) {
            console.log("Multiplication failure: "+ e);
        }
    }
}

console.log(multiplyAnyhow(2,3));



const box = new class {
    locked = true;
    #content = [];
  
    unlock() { this.locked = false; }
    lock() { this.locked = true;  }
    get content() {
      if (this.locked) throw new Error("Locked!");
      return this.#content;
    }
  };
  
  function withBoxUnlocked(body) {
    // Your code here.
    if (!box.locked) keepOpen = true
    else keepOpen = false
    try {
      box.unlock()
      body()
    } finally {
      if (!keepOpen) box.lock()
    }
    
  }
  
  withBoxUnlocked(() => {
    box.content.push("gold piece");
  });
  
  try {
    withBoxUnlocked(() => {
      throw new Error("Pirates on the horizon! Abort!");
    });
  } catch (e) {
    console.log("Error raised: " + e);
  }
  console.log(box.locked);
  // → true
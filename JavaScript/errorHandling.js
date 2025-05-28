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

// checkNumberPrompt("How old are you?");
// console.log(checkNumberPrompt("How old are you?"));

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

try {
    console.log(look());
} catch (error) {
    console.log("Something went wrong:" + error);    
}
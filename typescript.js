function greet(person, date) {
    console.log(`Hello ${person}, today is ${date}!`);
}
const user = "Jane User";
const date = new Date();
// greet(user, date);
let numArray = [];
let strArray = ["a", "b", "c", "d", "e"];
function printName(obj) {
    console.log(obj.first);
    console.log(obj.last ? obj.last.toUpperCase() : "No last name");
}
// printName({first: "John", last: "Doe"});
// printName({first: "Jane"});
function printId(id) {
    if (typeof id === "string") {
        console.log("Your ID is: " + id.toUpperCase());
    }
    else {
        console.log("Your ID is: " + id);
    }
}
// printId(101);
// printId("vikas srivastava");
function welcomePeople(people) {
    if (Array.isArray(people)) {
        console.log("Hello: " + people.join(", "));
    }
    else {
        console.log("Hello lonely guest: " + people);
    }
}
function printCoord(pt) {
    console.log(`X cordinate: ${pt.x}`);
    console.log(`Y cordinate: ${pt.y}`);
}
// printCoord({x: 100, y: 200});
function printDirection(driver, direction) {
    console.log(`Driver ${driver} is going to turn ${direction}`);
}
// printDirection("John", "left");
// printDirection("John", "up"); // Error: Argument of type '"up"' is not assignable to parameter of type '"left" | "right"'
// printDirection("John", "right");
function compare(a, b) {
    return a === b ? 0 : a > b ? 1 : -1;
}
// console.log(compare(10, 20)); // -1
// console.log(compare(20, 10)); // 1
// console.log(compare(10, 10)); // 0
function padLeft(padding, input) {
    if (typeof padding === "number") {
        return " ".repeat(padding) + input;
    }
    return padding + input;
}
// console.log(padLeft(4, "Hello"));
// console.log(padLeft("0000", "Hello"));
// console.log(padLeft(true, "Hello")); // Error: Argument of type 'boolean' is not assignable to parameter of type 'string | number'
function doSomething(x) {
    if (x !== null) {
        console.log(x.toUpperCase());
    }
}
function liveDangerously(x) {
    console.log(x.toFixed());
}
function isFish(pet) {
    return pet.swim !== undefined;
}
let fish = {
    "swim": () => void 
};
console.log(isFish(fish)); // true

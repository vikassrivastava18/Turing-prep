var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
// Basic primitives for TypeScript (string, numbers, boolean)
let isDone = false; // boolean
let fName; // string
let age = 30; // number
let school = "ABC School"; // string (No need to define type, TS will infer it by looking at the value).
// Arrays
let list = [1, 2, 3]; // array of numbers
let names = ["John", "Jane"]; // array of strings
let names2 = ["John", "Jane"]; // array of strings
let list2 = [1, "John", 2, "Jane"]; // array of strings and numbers
let list3 = [1, "John", 2, "Jane"]; // array of strings and numbers
/* Any type
  (Behaviour same as JS. Should always be avoided)
*/
let obj = { x: 0 };
// None of the following lines of code will throw compiler errors.
// Using `any` disables all further type checking, and it is assumed
// you know the environment better than TypeScript.
// obj.foo();
// obj();
// obj.bar = 100;
// obj = "hello";
// const n: number = obj;
/*
noImplicitAny
*/
// No error (Gives error when noImplicitAny is set to true)
function bad(s) {
    console.log(`Hello World!`);
}
// Function
function add(x, y) {
    return x + y;
}
// Function which returns a promise
function getData() {
    return __awaiter(this, void 0, void 0, function* () {
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                resolve("Data received");
            }, 1000);
        });
    });
}
getData().then((data) => {
    console.log(data);
}).catch((error) => {
    console.error(error);
});
// Object Types
function printCoordinates(pt) {
    console.log(`X: ${pt.x}, Y: ${pt.y}`);
}
// Optional properties
function printName(obj) {
    var _a;
    // Error - might crash if 'obj.last' wasn't provided!
    console.log(obj.last.toUpperCase());
    // 'obj.last' is possibly 'undefined'.
    if (obj.last !== undefined) {
        // OK
        console.log(obj.last.toUpperCase());
    }
    // A safe alternative using modern JavaScript syntax:
    console.log((_a = obj.last) === null || _a === void 0 ? void 0 : _a.toUpperCase());
}
function printName2(obj) {
    return obj.last ? `${obj.first} ${obj.last}` : `${obj.first}`;
}
console.log(printName2({ first: "John" })); // John
console.log(printName2({ first: "John", last: "Doe" })); // John Doe
// Union Types
function printId(id) {
    console.log(`ID: ${id}`);
}
function printId2(id) {
    // Check typ using 'typeof' operator
    if (typeof id === "string") {
        // In this branch, id is of type 'string'
        console.log(id.toUpperCase());
    }
    else {
        // Here, id is of type 'number'
        console.log(id);
    }
}
const welcomePeople = function (x) {
    if (Array.isArray(x)) {
        // Here: 'x' is 'string[]'
        console.log("Hello, " + x.join(" and "));
    }
    else {
        // Here: 'x' is 'string'
        console.log("Welcome lone traveler " + x);
    }
};
const welcomePeople2 = function (x) {
    if (Array.isArray(x)) {
        // Here: 'x' is 'string[]'
        console.log("Hello, " + x.join(" and "));
    }
    else {
        // Here: 'x' is 'string'
        console.log("Welcome lone traveler " + x);
    }
};
welcomePeople2("John"); // Welcome lone traveler John
welcomePeople2(["John", "Jane", "Mary"]); // Hello, John and Jane
function printPoint(pt) {
    console.log(`X: ${pt.x}, Y: ${pt.y}`);
}
function printPoint3D(pt) {
    console.log(`X: ${pt.x}, Y: ${pt.y}, Z: ${pt.z}`);
}
function printPoint2D(pt) {
    console.log(`X: ${pt.x}, Y: ${pt.y}`);
}
function printPoint3D2(pt) {
    console.log(`X: ${pt.x}, Y: ${pt.y}, Z: ${pt.z}`);
}
function move(direction) {
    console.log(`Moving ${direction}`);
}
function printText(s, alignment) {
    // ...
}
printText("Hello, world", "left");
//   printText("G'day, mate", "centre");
//   Argument of type '"centre"' is not assignable to parameter of type '"left" | "right" | "center"'.
function compare(a, b) {
    return a === b ? 0 : a > b ? 1 : -1;
}
const req = { url: "https://example.com", method: "GET" }; // Type assertion to "GET"
// handleRequest(req.url, req.method as "GET"); // Type assertion to "GET"
// ENUMS
var Direction;
(function (Direction) {
    Direction["Up"] = "up";
    Direction["Down"] = "down";
    Direction["Left"] = "left";
    Direction["Right"] = "right";
})(Direction || (Direction = {}));
console.log(move(Direction.Down));
var Direction2;
(function (Direction2) {
    Direction2[Direction2["Up"] = 0] = "Up";
    Direction2[Direction2["Down"] = 1] = "Down";
    Direction2[Direction2["Left"] = 2] = "Left";
    Direction2[Direction2["Right"] = 3] = "Right";
})(Direction2 || (Direction2 = {}));
console.log(Direction.Up); // "up"
console.log(Direction2.Up); // 0
console.log(Direction["Up"]); // Up
var UserResponse;
(function (UserResponse) {
    UserResponse[UserResponse["No"] = 0] = "No";
    UserResponse[UserResponse["Yes"] = 1] = "Yes";
})(UserResponse || (UserResponse = {}));
function respond(recipient, message) {
    console.log(`To: ${recipient}, Message: ${message}`);
}
respond("Princess Caroline", UserResponse.Yes);
//   STRING ENUMS
var Direction3;
(function (Direction3) {
    Direction3["Up"] = "UP";
    Direction3["Down"] = "DOWN";
    Direction3["Left"] = "LEFT";
    Direction3["Right"] = "RIGHT";
})(Direction3 || (Direction3 = {}));

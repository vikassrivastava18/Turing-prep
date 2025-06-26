// Basic primitives for TypeScript (string, numbers, boolean)
let isDone: boolean = false; // boolean
let fName: string // string
let age: number = 30; // number
let school = "ABC School"; // string (No need to define type, TS will infer it by looking at the value).


// Arrays
let list: number[] = [1, 2, 3]; // array of numbers
let names: string[] = ["John", "Jane"]; // array of strings
let names2: Array<string> = ["John", "Jane"]; // array of strings
let list2: (string | number)[] = [1, "John", 2, "Jane"]; // array of strings and numbers
let list3: Array<string | number> = [1, "John", 2, "Jane"]; // array of strings and numbers


/* Any type 
  (Behaviour same as JS. Should always be avoided)
*/
let obj= { x: 0 };
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
function add(x: number, y: number): number {
    return x + y;
}

// Function which returns a promise
async function getData(): Promise<string> {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve("Data received");
        }, 1000);
    });
}

getData().then((data) => {
    console.log(data);
}).catch((error) => {
    console.error(error);
});


// Object Types
function printCoordinates(pt: {x: number, y: number}) {
    console.log(`X: ${pt.x}, Y: ${pt.y}`);
}

// Optional properties
function printName(obj: { first: string; last?: string }) {
    // Error - might crash if 'obj.last' wasn't provided!
    console.log(obj.last.toUpperCase());
    // 'obj.last' is possibly 'undefined'.
    if (obj.last !== undefined) {
      // OK
      console.log(obj.last.toUpperCase());
    }
    // A safe alternative using modern JavaScript syntax:
    console.log(obj.last?.toUpperCase());
}

function printName2(obj: { first: string; last?: string }): string {
    return obj.last? `${obj.first} ${obj.last}` : `${obj.first}`; 
}

console.log(printName2({ first: "John" })); // John
console.log(printName2({ first: "John", last: "Doe" })); // John Doe

// Union Types
function printId(id: number | string) {
    console.log(`ID: ${id}`);
}

function printId2(id: number | string) {
    // Check typ using 'typeof' operator
    if (typeof id === "string") {
      // In this branch, id is of type 'string'
      console.log(id.toUpperCase());
    } else {
      // Here, id is of type 'number'
      console.log(id);
    }
}

const welcomePeople = function (x: string[] | string) {
    if (Array.isArray(x)) {
      // Here: 'x' is 'string[]'
      console.log("Hello, " + x.join(" and "));
    } else {
      // Here: 'x' is 'string'
      console.log("Welcome lone traveler " + x);
    }
}


const welcomePeople2 = function (x: string[] | string) {
    if (Array.isArray(x)) {
      // Here: 'x' is 'string[]'
      console.log("Hello, " + x.join(" and "));
    } else {
      // Here: 'x' is 'string'
      console.log("Welcome lone traveler " + x);
    }
}

welcomePeople2("John"); // Welcome lone traveler John
welcomePeople2(["John", "Jane", "Mary"]); // Hello, John and Jane


// TYPE ALIAS
type Point = { x: number; y: number };
type Point3D = Point & { z: number }; // Intersection type

function printPoint(pt: Point): void {
    console.log(`X: ${pt.x}, Y: ${pt.y}`);
}

function printPoint3D(pt: Point3D): void {
    console.log(`X: ${pt.x}, Y: ${pt.y}, Z: ${pt.z}`);
}

// INTERFACE
interface Point2D {
    x: number;
    y: number;
}
interface Point3D2 extends Point2D {    
    z: number;
}
function printPoint2D(pt: Point2D): void {
    console.log(`X: ${pt.x}, Y: ${pt.y}`);
}
function printPoint3D2(pt: Point3D2): void {
    console.log(`X: ${pt.x}, Y: ${pt.y}, Z: ${pt.z}`);
}

// LITERALS
type MovementDirection = "up" | "down" | "left" | "right";

function move(direction: MovementDirection) {
    console.log(`Moving ${direction}`);
}

function printText(s: string, alignment: "left" | "right" | "center") {
    // ...
  }
printText("Hello, world", "left");
//   printText("G'day, mate", "centre");
//   Argument of type '"centre"' is not assignable to parameter of type '"left" | "right" | "center"'.
  
function compare(a: number, b: number): 0 | 1 | -1 {
    return a === b ? 0 : a > b ? 1 : -1;
}


declare function handleRequest(url: string, method: "GET" | "POST"): void;

const req = { url: "https://example.com", method: "GET" as "GET" }; // Type assertion to "GET"
// handleRequest(req.url, req.method as "GET"); // Type assertion to "GET"


// STRING ENUMS
enum Direction {
    Up = "up", 
    Down = "down", 
    Left = "left",
    Right = "right"
}
console.log(move(Direction.Down));


// DEFAULT ENUMS
enum Direction2 {
    Up,
    Down,
    Left,
    Right
}

console.log(Direction.Up); // "up"
console.log(Direction2.Up); // 0
console.log(Direction["Up"]); // Up


enum UserResponse {
    No = 0,
    Yes = 1,
  }
   
  function respond(recipient: string, message: UserResponse): void {
    console.log(`To: ${recipient}, Message: ${message}`);
  }
   
  
  respond("Princess Caroline", UserResponse.Yes);


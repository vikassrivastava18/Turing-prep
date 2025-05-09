function greet(person: string, date: Date) {
    console.log(`Hello ${person}, today is ${date}!`);
}

const user = "Jane User";
const date = new Date();
// greet(user, date);

let numArray: number[] = [];
let strArray: string[] = ["a", "b", "c", "d", "e"];

function printName(obj: { first: string, last?: string }) {
    console.log(obj.first);
    console.log(obj.last ? obj.last.toUpperCase() : "No last name");
}

// printName({first: "John", last: "Doe"});
// printName({first: "Jane"});

function printId(id: number | string) {
    if (typeof id === "string") {
        console.log("Your ID is: " + id.toUpperCase());
    }
    else {
        console.log("Your ID is: " + id);
    }
}

// printId(101);
// printId("vikas srivastava");

function welcomePeople(people: string[] | string) {
    if (Array.isArray(people)) {
        console.log("Hello: " + people.join(", "));
    }
    else {
        console.log("Hello lonely guest: " + people);
    }
}

// welcomePeople(["John", "Jane", "Doe"]);
// welcomePeople("Vikas Srivastava");

interface Point {
    x: number;
    y: number;
}

function printCoord(pt: Point) {
    console.log(`X cordinate: ${pt.x}`);
    console.log(`Y cordinate: ${pt.y}`);
}

// printCoord({x: 100, y: 200});

function printDirection(driver: string, direction: "left" | "right") {
    console.log(`Driver ${driver} is going to turn ${direction}`);
}
// printDirection("John", "left");
// printDirection("John", "up"); // Error: Argument of type '"up"' is not assignable to parameter of type '"left" | "right"'
// printDirection("John", "right");

function compare(a: number, b: number): -1 | 0 | 1 {
    return a === b ? 0 : a > b ? 1 : -1
}

// console.log(compare(10, 20)); // -1
// console.log(compare(20, 10)); // 1
// console.log(compare(10, 10)); // 0


function padLeft(padding: string | number, input: string) {
    if (typeof padding === "number") {
        return " ".repeat(padding) + input;
    }
    return padding + input;
}

// console.log(padLeft(4, "Hello"));
// console.log(padLeft("0000", "Hello"));
// console.log(padLeft(true, "Hello")); // Error: Argument of type 'boolean' is not assignable to parameter of type 'string | number'

function doSomething(x: string | null) {
    if (x !== null) {
        console.log(x.toUpperCase());
    }
}

function liveDangerously(x?: number | null) {
    console.log(x!.toFixed());
}

// liveDangerously(100);
// doSomething(null); // Error: Object is possibly 'null'.
interface Fish {
    swim: () => void
}

interface Bird {
    fly: () => void
}

function isFish(pet: Fish | Bird): pet is Fish {
    return (pet as Fish).swim !== undefined;
}

let fish = {
    "swim": () => console.log("swimming")
};
console.log(isFish(fish)); // true


function swap<T, U>(tuple: [T, U]): [U, T] {
    return [tuple[1], tuple[0]];
}

function swapEasy(num1: number, num2: number): [number, number] {
    return [num2, num1];
}

console.log(swap([1, "a"])); // ["a", 1]
console.log(swapEasy(1, 2)); // [2, 1]


// Tuples
let newNumber: [number, number] = swapEasy(11, 21);
// console.log(newNumber[2]); // [21, 11]


// Functions (Always add return type!)

// Named function
function add(x: number, y: number): number {
    return x + y;
}

//Function expression
const add2 = function (x: number, y: number): number {
    return x + y;
}

// Arrow function
const multiply = (x: number, y: number): number => x * y
console.log(multiply(10, 20)); // 200

// Optional parameters
function add3(x: number, y: number, z?: number): number {
    return z ? x + y + z : x + y;
}

// Default parameters
function add4(x: number, y: number, z: number = 0): number {
    return x + y + z;
}

console.log(add4(10, 20)); // 30
console.log(add4(10, 20, 30)); // 60

// Classes
class Product {
    id: number;
    name: string;
    price: number;
    category: string;

    constructor(id: number, name: string, price: number, category: string) {
        this.id = id;
        this.name = name;
        this.price = price;
        this.category = category;
    }

    getDetails(): string {
        return `Product ID: ${this.id}, Name: ${this.name}, Price: ${this.price}, Category: ${this.category}`;
    }

}

// console.log(new Product(1, "Laptop", 1000, "Electronics").getDetails()); // Product ID: 1, Name: Laptop, Price: 1000, Category: Electronics

class Product2 {
    private _id: number;
    name: string;
    price: number;
    category: string;

    constructor(name: string, price: number, category: string) {
        this.name = name;
        this.price = price;
        this.category = category;
    }

    getDetails(): string {
        return `Product Name: ${this.name}, Price: ${this.price}, 
                Category: ${this.category}`;
    }

    get id(): number {
        return this._id;
    }

    set id(value: number) {
        this._id = value
    }
}

let product = new Product2("Laptop", 1000, "Electronics");
console.log(product.getDetails()); // Product Name: Laptop, Price: 1000, Category: Electronics

product.id = 1;

// Inheritance

class Mobile extends Product2 {
    constructor(name: string, price: number, category: string) {
        super(name, price * 10, category);
    }

    getDetails(): string {
        return `Mobile name: ${this.name}, Price: ${this.price}`;
    }
}

let mobile = new Mobile("iPhone", 1000, "Electronics");
console.log(mobile.getDetails()); // Mobile name: iPhone, Price: 1000

interface Address {
    addressLine1: string;
    addressLine2?: string;
    city: string;
    country: string;
}

let addres: Address = {
    addressLine1: "123 Main St",
    // addressLine2: "Apt 4B",
    city: "New York",
    country: "USA"
}

interface Employees {
    id: number;
    name: string;
    department: string;
    salary: number;
    email: string;
    dob: Date;
}

let empList : Employees[] = [
    {
        id: 1,
        name: "John Doe",
        department: "IT",
        salary: 50000,
        email: "vikas@gmail.com",
        dob: new Date("1990-01-01")
    },
    {
        id: 2,
        name: "Jane Smith",
        department: "HR",
        salary: 60000,
        email: "Jane@yopmail.com",
        dob: new Date("1992-02-02")
    }
]

let findRichEmployees = empList.filter(emp => emp.salary > 50000);
console.table(findRichEmployees);

let averageSalary = empList.reduce((acc, emp) => acc + emp.salary, 0) / empList.length;
console.log(averageSalary);

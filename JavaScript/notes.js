// REGEX 
let aPlus = /A\+/; // + is a regex operator and we want to match with + as character
console.log(aPlus.test("I scored an A+ in Math.")); // true
console.log(/[0-9]/.test("I got a 90 in Math.")); // true

// Match negation
// w: Word character including a-z, A-Z, 0-9
console.log(/\W/.test("12345")); // false
console.log(/\W/.test("12@45")); // true
console.log(/\W/.test("hello")); // false
console.log(/\D/.test("12345")); // false

/*
+ One or more
* Zero or more
? Optional
*/

console.log(/\d+/.test("123")); // true
console.log(/\d*/.test("hello")); // true
console.log(/neighbou?r/.test("neighbour"));// true (also neighbor)

// Matches and Subgroups
let match = /\d+/.exec("He scored a 100") // 100
let domain = /@.*/.exec("vikas@gmail.com") // @gmail.com
console.log(match); // .index gives the index of match
console.log(domain);

console.log(/'[^']*'/.exec("She said: 'I am going!'"));

// Replace, ReplaceAll (String methods)
console.log("papa".replace("p", "m")); // mapa
console.log("papa".replaceAll("p", "m")); // mama


// SLICE
let arr = [1,2,3]
console.log(arr.slice(0,-1))
/*
array.slice(start, end)
start (optional): The index at which to begin extraction. Defaults to 0 if omitted.

end (optional): The index before which to end extraction. The element at this index is not included. If omitted, it slices till the end of the array.

❗ Negative indices count from the end of the array: -1 refers to the last element, -2 to the second last, and so on.
*/

// Includes
const obj = {name: "vikas", age: 38}
console.log(Object.keys(obj).includes("name"));
console.log(Object.values(obj).includes("prakash"));

// IndexOf: used in both strings and Arrays
let arrNew = [1,2,3,4];
console.log(arrNew.indexOf(2)); // 1
let nameNew = "vikas"
console.log(nameNew.indexOf("ka")); // 2

// Optional Arguments

function minus(a, b) {
    /* 1)
    if (b === undefined) return -a
    return a - b;
      2)
    
    */
    return b ? a - b : -1
}

console.log("Difference: ", minus(4,1));
console.log("Difference: ", minus(4));


// Default Arguments
function sayHello(name="Vikas") {
    console.log(`Hello: ${name}`);    
}

// Closure

function wrapValue(n) {
    let local = n;
    return () => local;
}

let wrap1 = wrapValue(1);
let wrap2 = wrapValue(2)
console.log(wrap1());
console.log(wrap2());


function multiplier(factor) {
    return number => number * factor
}

let twice = multiplier(2);
console.log(twice(10));
console.log(twice(5));


// Recursion 
function power(base, exponent) {
    if (exponent === 0) return 1
    return base * power(base, exponent-1)
}

console.log("Power of 2 to 3: ", power(2,3));

// Check evenness using recursion
function isEven(num) {
    if  (num < 0) return '??'
    else if (num === 1) return false 
    else if (num === 0) return true

    return isEven(num-2)
}

console.log(isEven(50));
// → true
console.log(isEven(75));
// → false
console.log(isEven(-1));
// → ??

// Count the number of B's in a word
function countBs(word) {
    let count = 0;
    for (let char of word) {
        if (char === 'B') count += 1
    }
    return count
}

function countChar(word, c) {
    let count = 0;
    for (let char of word) {
        if (char === c) count += 1
    }
    return count
}

console.log(countBs("BOB"));
// → 2
console.log(countChar("kakkerlak", "k"));
// 4
// Destructuring

function phi([n00, n01, n10, n11]) {
    const corr = (n11 * n00 - n10 * n01) / (Math.sqrt((n10 + n11) * (n00 + n01) * (n01 + n11) * (n00 + n10)))
    return corr
}

console.log(phi([76, 9, 4, 1]));

// Rest Parameters
function max(...numbers) {
    let max = -Infinity

    for (let num of numbers) {
        if (num > max) max = num
    }
    return max
}

console.log(max(4,1,9,-2));

// Spread operation
let numbers = [5, 1, 7];
console.log(max(...numbers));
console.log(max(9, ...numbers, 2));

let words = ["never", "fully"];
console.log(["We", "will", ...words, "understand"]);


// Shift, Unshift
// removes and add first item in an array respectively.

let toDoList = ["study", "pray"];
toDoList.shift()
console.log(toDoList);
toDoList.unshift("work")
console.log(toDoList);













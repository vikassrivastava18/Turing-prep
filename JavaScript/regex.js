/*
 Regular Expression
 Create a regular expression object: 
*/

let aPlus = /A\+/;
console.log(aPlus.test("I got A+ in Math."))
console.log(aPlus.test("I got A in Math."))

// Match a number in a string
console.log(/[0-9]/.test("I got a 90 in Math")); // true
console.log(/[0-9]/.test("I got a A in Math")); // false

// Match a alphanumeric character
console.log(/\w/.test("hello world")); // true
console.log(/\W/.test("Hello world")); // true due to space (W means negation)
console.log(/\W/.test("Hello")); // false
// Match a digit character
console.log(/\d/.test("hello 2025")); // true
console.log(/\D/.test("2025")); // false

/*
{} -> Number of repetitions
Match a date format
*/
let dateFormat = /\d{2}-\d{2}-\d{4}/;
let dateFormatFlexible = /\d{1,2}-\d{1,2}-\d{4}/;
console.log(dateFormat.test("02-06-2025")); // true
console.log(dateFormatFlexible.test("2-6-2025")); // true
console.log(dateFormatFlexible.test("2-6-25")); // false

/*
[] -> possible match
*/
console.log(/[\d.]/.test("hello world.")); // true
console.log(/[\d.]/.test("hello 123")); // true
console.log(/[\d.]/.test("hello world")); // false
// Match non binaries
let nonBinaries = /[^01]/;
console.log(nonBinaries.test("0001101010101")); // false
console.log(nonBinaries.test("0001101010801")); // true due to 8

/*
+ One or more -> "'123'"
* Zero or more -> "''"
? Optional -> "neighbou?r"
*/
console.log(/\d+/.test("123")); // true
console.log(/\d*/.test("hello")); // true
console.log(/neighbou?r/.test("neighbor")); // true
console.log(/o+k+/.test("oooookk")); // true


const dateTime = /\d{2}-\d{2}-\d{4} \d{2}:\d{2}/;
console.log(dateTime.test("02-04-2023 12:5")) // false


// Grouping subexpressions
const cartoonCrying = /boo+(hoo+)+/i;
console.log(cartoonCrying.test("Booohoohoooo")); // true


// Matches and Subgroups
let match = /\d+/.exec("He scored a 100");
console.log(match);
console.log(match.index);

let domain = /@.*/.exec("vikas@gmail.com")
console.log(domain);





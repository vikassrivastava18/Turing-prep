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















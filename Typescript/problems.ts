function checkBrackets(str: string): boolean {
    // Function accepts a string a returns if all the brackets are properly closed.
    const openBrackets: string[] = ["{", "(", "["];
    const closedBrackets: string[] = ["}", ")", "]"];
    let testBucket:string[] = [];

    for (let char of str) {
        if (openBrackets.includes(char)) {
            testBucket.push(char);
        } 
        else if (closedBrackets.includes(char)) {
            if (testBucket.length === 0) return false
            else {
                const lastBracket = testBucket[testBucket.length-1]
                if (openBrackets.indexOf(lastBracket) != closedBrackets.indexOf(char)) return false
                testBucket = testBucket.slice(0, -1)
            }
        }                
    }
    return true
}

// Test cases to pass
console.log(checkBrackets("{([])}"))
console.log(checkBrackets("hello{]}"))

function countSqRoots(numList: number[]): number[] {
    // Function returns all elements in Array that have square roots in the Array(including iteself)
    let output: number[] = [];
    for (let num of numList) {
        if (numList.includes(num ** 2)) output.push(num)
    }

    return output
}

console.log(countSqRoots([1,2,3,4,5]));


function removeAndSort(numList: number[], k: number): number[] {
    // Remove all the items in array before k, the return sorted Array
    let removedArray = numList.slice(k, numList.length);
    const sortedArray = removedArray.sort((a, b) => a - b);

    return sortedArray
    
}

console.log(removeAndSort([1,2,30,14,5], 2));


function sameChars(w1: string, w2: string): boolean {
    // Returns true if both words contain same characters irrespective of frequency
    const uniqueFirst = Array.from(new Set(w1)).sort().join("");
    const uniqueSecond = Array.from(new Set(w2)).sort().join("");

    return uniqueFirst === uniqueSecond
}

console.log(sameChars("hello", "hellllooo"));
console.log(sameChars("abcd", "acbd"));
console.log(sameChars("abcd", "acbe"));


const binarySearchFunc = function(l: number[], n: number): number {
    let startInd = 0; let endIndex = l.length-1;
    let midInd: number = Math.floor((startInd + endIndex) / 2)

    while (startInd <= endIndex) {
        if (l[midInd] == n) return midInd

        else if (l[midInd] < n) startInd = midInd + 1;

        else endIndex = midInd - 1;
        
        midInd = Math.floor((startInd + endIndex) / 2)
    }

    return -1
}


console.log(binarySearchFunc([5,14,30], 14));
console.log(binarySearchFunc([5,14,30], 5));
console.log(binarySearchFunc([5,14,30], 30));
console.log(binarySearchFunc([5,14,30], -14));


const guessInBillion = function(): number[] {
    const numToGuess = Math.floor(Math.random() * 1_000_000_001);
    
    let start = 0; 
    let end = 1_000_000_000;
    let guess = Math.floor((start + end) / 2)
    let attempts = 0

    while (guess !== numToGuess) {
        attempts += 1;

        if (guess < numToGuess) start = guess + 1;
        else end = guess - 1;
        guess = Math.floor((start + end) / 2)
    }

    return ([numToGuess, guess, attempts])

}

console.log(guessInBillion());

const flatten = function(l): number[] {
    let result: number[] = [];

    for (let item of l) {        
        if (typeof item === "number") result.push(item)
    
        else result = result.concat(flatten(item))        
    }

    return result
}

console.log(flatten([1,2,3,[4,5,[6,7]]]));

const twoSum =(l: number[], s: number): Array<number[]> => {
    //  Returns a list of pairs whose sum = s
    //  Array is sorted
    let result: Array<number[]> = [];
    let start = 0;
    let end = l.length - 1;

    while (start < end) {
        if (l[start] + l[end] == s) {
            result.push([l[start], l[end]])
            start += 1;
            end -= 1;
        }
        
        else if (l[start] + l[end] < s) start += 1

        else end -= 1;
    }

    return result
}

console.log(twoSum([0,1,2,3,4,5], 4));
console.log(twoSum([0,1,2,3,4,5], 5));
console.log(twoSum([0,1,2,3,4,5], 15));


const longestSubstringCount = function(str: string): number {
    let subSet: Set<string> = new Set();
    let left = 0;
    let maxLength = 0;

    for (let right=0; right < str.length; right++) {
        while (subSet.has(str[right])) {
            subSet.delete(subSet.values().next().value);
            left +=1
        }

        subSet.add(str[right])
        maxLength = Math.max(maxLength, right - left + 1)
    }

    return maxLength
}

console.log(longestSubstringCount("abcdaaf"));

const fibonacci = (n: number): number => {
    if (n === 0 || n === 1 ) return n
    let a = 0;
    let b = 1;
    let count = 2

    while (count <= n) {
        let r = a + b
        a = b;
        b = r;
        count +=1
    }
    return b
}


const groupAnagram = function (arr:  string[]): Array<string[]> {
    let out = {}
    for (let word of arr) {
        const wordSorted = word.split('').sort().join('');

        if (wordSorted in out) out[wordSorted].push(word)
        else out[wordSorted] = [word]
    }

    return Object.values(out)
}

console.log(groupAnagram(["eat", "tea", "ate", "pan", "nap"]));

String var company: string = "a";
Number var age: number = 10
Boolean var b: booleam = false
console.log([1].indexOf(1200));

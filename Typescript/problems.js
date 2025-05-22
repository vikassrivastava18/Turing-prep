function checkBrackets(str) {
    // Function accepts a string a returns if all the brackets are properly closed.
    const openBrackets = ["{", "(", "["];
    const closedBrackets = ["}", ")", "]"];
    let testBucket = [];
    for (let char of str) {
        if (openBrackets.includes(char)) {
            testBucket.push(char);
        }
        else if (closedBrackets.includes(char)) {
            if (testBucket.length === 0)
                return false;
            else {
                const lastBracket = testBucket[testBucket.length - 1];
                if (openBrackets.indexOf(lastBracket) != closedBrackets.indexOf(char))
                    return false;
                testBucket = testBucket.slice(0, -1);
            }
        }
    }

    return testBucket.length === 0
}
// Test cases to pass
console.log("------------------");

console.log(checkBrackets("{([])}"));
console.log(checkBrackets("hello{]}"));

console.log("------------------");

function countSqRoots(numList) {
    // Function returns all elements in Array that have square roots in the Array(including iteself)
    let output = [];
    for (let num of numList) {
        if (numList.includes(num ** 2))
            output.push(num);
    }
    return output;
}
console.log(countSqRoots([1, 2, 3, 4, 5]));

function removeAndSort(numList, k) {
    // Remove all the items in array before k, the return sorted Array
    let removedArray = numList.slice(k, numList.length);
    const sortedArray = removedArray.sort((a, b) => a - b);
    return sortedArray;
}
console.log(removeAndSort([1, 2, 30, 14, 5], 2));

function sameChars(w1, w2) {
    const uniqueFirst = new Set(w1);
    const uniqueSecond = new Set(w2);
    const firstArray = Array.from(uniqueFirst);
    const secondArray = Array.from(uniqueSecond);
    if (firstArray.length != secondArray.length)
        return false;
    for (let chars of firstArray) {
        if (!secondArray.includes(chars))
            return false;
    }
    return true;
}
const w1 = "hello";
const w2 = "hellllooo";
const w3 = "abcd";
const w4 = "abce";
console.log(sameChars(w1, w2));
console.log(sameChars(w3, w4));

const binarySearchFunc = function (l, n) {
    let startInd = 0;
    let endIndex = l.length - 1;
    let midInd = Math.floor((startInd + endIndex) / 2);
    while (startInd <= endIndex) {
        if (l[midInd] == n)
            return midInd;
        else if (l[midInd] < n)
            startInd = midInd + 1;
        else
            endIndex = midInd - 1;
        midInd = Math.floor((startInd + endIndex) / 2);
    }
    return -1;
};
console.log(binarySearchFunc([5, 14, 30], 14));
console.log(binarySearchFunc([5, 14, 30], 5));
console.log(binarySearchFunc([5, 14, 30], 30));
console.log(binarySearchFunc([5, 14, 30], -14));

const guessInBillion = function () {
    const numToGuess = Math.floor(Math.random() * 1000000001);
    let start = 0;
    let end = 1000000000;
    let guess = Math.floor((start + end) / 2);
    let attempts = 0;
    while (guess !== numToGuess) {
        attempts += 1;
        if (guess < numToGuess)
            start = guess + 1;
        else
            end = guess - 1;
        guess = Math.floor((start + end) / 2);
    }
    return ([numToGuess, guess, attempts]);
};
console.log(guessInBillion());



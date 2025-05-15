function checkBrackets(str) {
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
    return true;
}
// Test cases to pass
console.log(checkBrackets("{([])}"));
console.log(checkBrackets("hello{]}"));
function countSqRoots(numList) {
    let output = [];
    for (let num of numList) {
        if (numList.includes(num ** 2))
            output.push(num);
    }
    return output;
}
console.log(countSqRoots([1, 2, 3, 4, 5]));
function removeAndSort(numList, k) {
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

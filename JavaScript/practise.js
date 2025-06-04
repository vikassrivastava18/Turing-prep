function wordWithoutVowel(sentence) {
    function checkVowel(word) {
        const vowels = ["a", "e", "i", "o", "u"];
        for (let letter of word) {
            if (vowels.includes(letter)) return true
        }
        return false
    }

    let result = [];
    for (let word of sentence) {
        // console.log(word, checkVowel(word));
        if (!checkVowel(word)) result.push(word)
    }
    return result.join(" ")
}

console.log(wordWithoutVowel("aa bb cc dd ee"));

function reverse(word) {
    wordArray = word.split("")
    wordArray = wordArray.reverse()
    wordArray = wordArray.join("")
    return wordArray
}

console.log(reverse("hello"));

function isPalindrome(word) {
    return word === reverse(word)
}

console.log(isPalindrome("hello"));
console.log(isPalindrome("malayalam"));


function repeatingWordsCount(sentence) {
    let uniqueWords = new Set(sentence.split(" "))
    return sentence.split(" ").length - Array.from(uniqueWords).length
}

let uniqueWords = "Once upon a time there was a bear in the jungle the end"
console.log(repeatingWordsCount(uniqueWords));

function repeatingWords(sentence) {
    let result = {};

    for (let word of sentence.split(" ")) {
        if (Object.keys(result).includes(word)) result[word] += 1
        else result[word] = 1
    }

    return result
}

console.log(repeatingWords(uniqueWords))

function palindrome(word) {
    // Returns true if the word is a palindrome
    let wordArray = word.split("");
    let wordArrayReverse = [...wordArray].reverse();

    return wordArray.join("") === wordArrayReverse.join("");
}

console.log(palindrome("malayalam"));
console.log(palindrome("hello"));


function anagram(w1, w2) {
    //  Returns true if w2 is a shuffled version of w1
    let w1Arr = w1.split("");
    let w2Arr = w2.split("");

    w1ArrSorted = [...w1Arr].sort()
    w2ArrSorted = [...w2Arr].sort()

    return w1ArrSorted.join("") === w2ArrSorted.join("")
}

console.log(anagram("appa", "papa"));
console.log(anagram("poop", "oopp"));
console.log(anagram("appa", "papo"));


function anagramOptimal(w1, w2) {
    return w1.split("").sort().join("") === w2.split("").sort().join("")
}

console.log(anagramOptimal("appa", "papa"));
console.log(anagramOptimal("poop", "oopp"));
console.log(anagramOptimal("appa", "papo"));


function anagramPairs(arr) {
    let result = {};

    for (let word of arr) {
        const wordRoot = word.split("").sort().join("")
        if (Object.keys(result).includes(wordRoot)) result[wordRoot].push(word)
        else result[wordRoot] = [word]
    }

    return Object.values(result)
}

console.log("Ana Pairs: ", anagramPairs(["eat", "tea", "ate", "pan", "nap"]));


function flatten(arr) {
    let result = [];

    for (let element of arr) {
        if (!Array.isArray(element)) result.push(element)
        else result = result.concat(flatten(element))
    }

    return result
}

console.log(flatten([1, 2, 3, [4, 5]])); // -> [1,2,3,4,5]
console.log(flatten([1, 2, 3, [4, "a", ["b", "c"]]])); // -> [1,2,3,4,"a", "b", "c"]

function stringLength(str) {
    let count = 0;

    for (let el of str) {
        if (Array.isArray(el)) count += stringLength(el)
        else count += el.length
    }

    return count
}

console.log("String length: ", stringLength(["abcd", "e", "fg", ["abcd", ["e", "fg"]]]));


function twoSum(arr, s) {
    /* Returns the pair of numbers that sum to s
    Array is sorted */
    let result = []
    let start = 0;
    let end = arr.length - 1

    while (start < end) {
        if (arr[start] + arr[end] == s) {
            result.push([arr[start], arr[end]])
            start += 1;
            end -= 1;
        }
        else if (arr[start] + arr[end] < s) start += 1;
        else end -= 1;
    }

    return result
}

console.log(twoSum([1, 2, 3, 4, 5], 7));
console.log(twoSum([1, 2, 3, 4, 5, 6], 7));


function threeSum(arr, s) {
    let result = [];

    for (let first = 0; first < arr.length - 1; first++) {
        let second = first + 1;
        let third = arr.length - 1;

        while (second < third) {
            if (arr[first] + arr[second] + arr[third] === s) {
                result.push([arr[first], arr[second], arr[third]])
                second += 1;
                third -= 1;
            }
            else if ((arr[first] + arr[second] + arr[third] < s)) second += 1;
            else third -= 1
        }
    }

    return result
}

console.log("Three sum: ", threeSum([0, 1, 2, 3, 4, 5, 6], 8));


function separator(word) {
    let numbers = [];
    let characters = [];

    for (let char of word) {
        if (!isNaN(Number(char))) numbers.push(char)
        else characters.push(char)
    }

    return ([numbers, characters])
}

console.log(separator("hello123"));


function encodedString(str) {
    // "3[a]2[bc]5[a]","13[a]2[bc]5[a]", "2[abc3[de]]""
    let result = "";
    let i = 0;
    let digit;

    while (i < str.length) {
        
        if(!Number.isNaN(Number(char))) {
            digit = Number(str(i))
        }

        else {

        }
        

    }
}

function fibonacci(n) {
    if (n === 0 || n === 1) return n

    let a = 0;
    let b = 1;

    for (let i = 2; i <= n; i++) {
        let saver = a + b;
        a = b;
        b = saver;
    }

    return b
}

for (let i = 0; i <= 5; i++) {
    console.log(fibonacci(i));
}


function isPrime(n) {
    if (n === 1 || n === 0) return false
    else if (n === 2) return true
    else if (n < 0) return false

    for (let i = 2; i < n; i++) {
        if (n % i === 0) return false
    }

    return true
}

console.log("Checking Prime --------------");

for (let i = 0; i <= 15; i++) {
    console.log(i, isPrime(i));
}


function binarySearch(arr, num) {
    let st = 0;
    let end = arr.length-1;

    while (st < end) {
        let mid = Math.floor((st + end)/2);
        if (num === arr[mid]) return mid
        else if (num < arr[mid]) end = mid - 1
        else st = mid + 1
    }

    return -1
}

console.log(binarySearch([5, 14, 30], 14));
console.log(binarySearch([5, 14,20, 30], 20));
console.log(binarySearch([5, 14, 30], 10));

function checkBrackets(str) {
    const open = ["[", "{", "("];
    const closed = ["]", "}", ")"];

    let bucket = [];

    for (let char of str) {
        if (open.includes(char)) bucket.push(char)
        else if (closed.includes(char)) {
            if (bucket.length === 0) return false
            else {
                const lastOpen = bucket[bucket.length-1]
                if (open.indexOf(lastOpen) !== closed.indexOf(char)) return false
                bucket = bucket.slice(0,-1);
            }
        }
    }

    return bucket.length === 0
}

console.log(checkBrackets("{([])}"));
console.log(checkBrackets("hello{]}"));
console.log(checkBrackets("{([])}["));

var lan = [1,2,3]
lan.length = 0
lan.push(4)
console.log("lan",lan);

function isPrime(n) {
    // Check that number is at least 2
    // Use modulus to check condition for prime.
    if (n < 2) return false
    else if (n === 2) return true

    for (let i=2; i < n; i++) {
        if (n % i === 0) return false
    }
    return true
}

console.log(isPrime(2));
console.log(isPrime(3));
console.log(isPrime(4));
console.log(isPrime(5));


function sameChars(w1, w2) {
    let w1Set = new Set(w1);
    let w2Set = new Set(w2);

    if (w1Set.size !== w2Set.size) return false;

    for (let char of w1Set) {
        if (!w2Set.has(char)) return false;
    }
    return true;
}

console.log(sameChars("abba", "baba")); // true
console.log(sameChars("abba", "baca")); // false

function sameChars2(w1, w2) {
    w1Arr = w1.split()
    w2Arr = w2.split()
    w1Arr.sort
    w2Arr.sort()
    return w1Arr.join("") === w2Arr.join("")
}

console.log(sameChars2("abba", "baba")); // true
console.log(sameChars2("abba", "baca")); // false

function dotProduct(tA, tB) {
    let sum = 0;

    for (let i=0; i<tA.length; i++) {
        sum += tA[i] * tB[i]
    }
    return sum
}

console.log(dotProduct([1,2,3], [3,2,1]));

function countSquareRoots(numArr) {
    let result = [];
    
    for (let element of numArr) {
        if (numArr.includes(element ** 2)) result.push(element)
    }
    return result;
}

console.log(countSquareRoots([3,4,2,1,9,25]));


function fibonacciMemoised(n, memo={1: 1, 2: 1}) {
    /*
    Return fib of n if in memo
    Else return the sum of previous two
    Update the memo
    */

   if (Object.keys(memo).includes(n.toString())) return memo[n]
   fib1 = fibonacciMemoised(n-1, memo)
   fib2 = fibonacciMemoised(n-2, memo)
   memo[n] = fib1 + fib2
   return memo[n]
}

console.log(fibonacciMemoised(120));

function anagramNew(w1, w2) {
    //  Returns true if w2 is a shuffled version of w1
    let w1Arr = w1.split("");
    let w2Arr = w2.split("");

    w1ArrSorted = w1Arr.sort()
    w2ArrSorted = w2Arr.sort()

    return w1ArrSorted.join("") === w2ArrSorted.join("")
}

console.log(anagramNew("appa", "papa"));
console.log(anagramNew("poop", "oopp"));
console.log(anagramNew("appa", "papo"));


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

console.log("String length: ",stringLength(["abcd", "e", "fg", ["abcd", ["e", "fg"]]]));


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

for (let i = 0; i <=5; i++) {
    console.log(fibonacci(i));
}


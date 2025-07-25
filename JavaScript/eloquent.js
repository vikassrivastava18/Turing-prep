// The Lyncanthrope's Log

let journal = [
  {events: ["work", "touched tree", "pizza",
            "running", "television"],
   squirrel: false},
  {events: ["work", "ice cream", "cauliflower",
            "lasagna", "touched tree", "brushed teeth"],
   squirrel: false},
  {events: ["weekend", "cycling", "break", "peanuts",
            "beer"],
   squirrel: true},
  /* And so on... */
];

/*
Correlation Formula
ϕ =	n11•n00 − n10•n01 / (√ n1•n0•n•1n•0)
*/


function phi([n00, n01, n10, n11]) {
    const corr = (n10 * n00 - n10 * n01) / (Math.sqrt((n10 + n11) * (n00 + n01) * (n01 + n11) * (n00 + n10)))
    return corr
}
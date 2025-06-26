let animal = {
    eats: true
};
let rabbit = {
    jumps: true
};

rabbit.__proto__ = animal;

console.log(rabbit.eats);

let newAnimal = {
    eats: true,
    walk() {
        console.log("Animal walk");
    }
}

let newRabbit = {
    jumps: true,
    __proto__: newAnimal
};

newRabbit.walk()

let longEar = {
    earLength: 10,
    __proto__: newRabbit
};

longEar.walk()
console.log(longEar.eats);


let user = {
    name: "John",
    surname: "Smith",

    set fullName(value) {
        [this.name, this.surname] = value.split(" ");
    },
    get fullName() {
        return `${this.name} ${this.surname}`
    }
}

let admin  = {
    __proto__: user,
    isAdmin: true
};

console.log(admin.fullName);
admin.fullName = "Vikas Srivastava";
console.log(admin.fullName);
console.log(user.fullName);

let anima = {
    jumps: null
};

let rab = {
    __proto__: anima,
    jumps: true
};

console.log(rab.jumps);
delete rab.jumps;
console.log(rab.jumps);
delete anima.jumps;
console.log(rab.jumps);


let head = {
    glasses: 1
}

let table = {
    __proto__: head,
    pen: 3
};

let bed = {
    __proto__: table,
    sheet: 1,
    pillow: 2
};

let pockets = {
    __proto__: bed,
    money: 2000
};

console.log(pockets.pen);
console.log(bed.glasses);


let animal1 = {
  eat() {
    this.full = true;
  }
};

let rabbit1 = {
  __proto__: animal1
};

rabbit1.eat();
console.log(animal1.full);
console.log(rabbit1.full);

let hamster = {
  stomach: [],

  eat(food) {
    this.stomach.push(food);
  }
};

let speedy = {
  __proto__: hamster
};

let lazy = {
  __proto__: hamster
};

// This one found the food
speedy.eat("apple");
console.log( speedy.stomach ); // apple

// This one also has it, why? fix please.
console.log( lazy.stomach ); // apple

// let hamster = {

//   eat(food) {
//     if (this.stomach) stomach.push(food)
//     else this.stomach = [food]
//   }
// };

// let speedy = {
//   __proto__: hamster
// };

// let lazy = {
//   __proto__: hamster
// };

// // This one found the food
// speedy.eat("apple");
// console.log( speedy.stomach ); // apple

// // This one also has it, why? fix please.
// console.log( lazy.stomach ); // apple


let animal3 = {
  name: "Animal",
  eat() {
    console.log(`${this.name} eats.`);
  }
};

let rabbit3 = {
  __proto__: animal3,
  name: "Rabbit",
  eat() {
    // that's how super.eat() could presumably work
    this.__proto__.eat.call(this); // (*)
    // this.__proto__.eat(); // Will not pass the object name
    // super.eat() // This will give expected result
  }
};

rabbit3.eat(); // Rabbit eats.
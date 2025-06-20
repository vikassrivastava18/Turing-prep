class User {
    constructor(name) {
        this.name = name;
    }
    sayHi() {
        console.log(`Hi ${this.name}`);
    }
    get name() {
        return this._name
    }
    set name(value) {
        if (value.length < 4) {
            console.log("Name too small, can't assign");
            return
        }
        this._name = value
    }

}

let u1 = new User("Jon")
u1.sayHi()


class Button {
    constructor(value) {
        this.value = value;
    }

    click() {
        console.log(this.value);
    }
}

let button = new Button("hello");

// setTimeout(button.click, 1000); // undefined

class Button2 {
    constructor(value) {
        this.value = value;
    }

    click = () => {
        console.log(this.value);
    }
}

let button2 = new Button2("hello");

// setTimeout(button2.click, 1000);


// Class kinda equivalent
function User2(name) {
    this.name = name
}

User2.prototype.sayHi = function () {
    console.log(this.name);

}

user2 = new User2("vikas")
user2.sayHi()

function Clock({ template }) {

    let timer;

    function render() {
        let date = new Date();

        let hours = date.getHours();
        if (hours < 10) hours = '0' + hours;

        let mins = date.getMinutes();
        if (mins < 10) mins = '0' + mins;

        let secs = date.getSeconds();
        if (secs < 10) secs = '0' + secs;

        let output = template
            .replace('h', hours)
            .replace('m', mins)
            .replace('s', secs);

        console.log(output);
    }

    this.stop = function () {
        clearInterval(timer);
    };

    this.start = function () {
        render();
        timer = setInterval(render, 1000);
    };

}

// let clock = new Clock({ template: 'h:m:s' });
// clock.start();

class Clock2 {

    constructor(template) {
        this.template = template
    }

    render = () => {
        let date = new Date();

        let hours = date.getHours();
        let mins = date.getMinutes();
        let secs = date.getSeconds()
        if (hours < 10) hours = '0' + hours;
        if (mins < 10) mins = '0' + mins;
        if (secs < 10) secs = '0' + secs;
        console.log("Template: ", this.template);

        let output = this.template
            .replace('h', hours)
            .replace('m', mins)
            .replace('s', secs);
        console.log(output);
    }

    start = () => {
        this.render()
        this.timer = setInterval(this.render, 1000)
    }

    stop = () => {
        clearInterval(this.timer)
    }
}


// let clock2 = new Clock2('h:m:s');
// clock2.start();
// setTimeout(clock2.stop, 5000)

// Class Based Inheritance

class Animal {

    constructor(name) {
        this.name = name;
        this.speed = 0
    }

    run(speed) {
        this.speed = speed
        console.log(`${this.name} runs at ${this.speed}.`);        
    }

    stop() {
        this.speed = 0;
        console.log(`${this.name} is now stationary.`);
        
    }
}

a = new Animal("Jack")
a.run(20)
a.stop()


class Rabbit extends Animal {

    /*
    Default behaviour for constructor
    constructor(...args) {
        super(...args);    
    }
    */
    constructor(name, earLength) {
        super(name);
        this.earLength = earLength
    }

    details () {
        console.log(`${this.name} has an ear of length ${this.earLength}`);
        
    }

    hide() {
        console.log(`${this.name} is now hiding!`);        
    }
    stop() {
        setTimeout(() => super.stop(), 1000);
    }
}

let rabbit = new Rabbit("White Rabbit", 20);

rabbit.run(5)
rabbit.hide()
rabbit.stop()
rabbit.details()


class Animal3 {

  constructor(name) {
    this.name = name;
  }

}

class Rabbit3 extends Animal3 {
  constructor(name) {
    super(name)
    this.created = Date.now();
  }
}

let rabbit3 = new Rabbit3("Whitish Rabbit"); // Error: this is not defined
console.log(rabbit3.name);


class ExtendedClock extends Clock2 {
    constructor(template, percision=1000) {
        super(template)
        console.log("percision", percision);
        this.percision = percision
    }

    start = () => {
        this.render()
        this.timer = setInterval(this.render, this.percision)
    }

    start() {
        this.render();
        this.timer = setInterval(() => this.render(), this.precision);
    }
}

let extClock = new ExtendedClock('h:m:s', 2000)
extClock.start();
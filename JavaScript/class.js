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


let clock2 = new Clock2('h:m:s');
clock2.start();
setTimeout(clock2.stop, 5000)
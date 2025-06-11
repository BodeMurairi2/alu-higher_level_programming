#!/usr/bin/node

// empty class
class Person {}

// add constructor
class Persons {

    name;

    constructor(name){
        this.name = name;
    }

    introduce_self(){
        console.log(`Hey there! I am ${this.name}`)
    }
}

class Professors extends Persons {
    teaches;

    constructor(name, teaches) {
        super(name);
        this.teaches = teaches;
    }

    introduce_self(){
        console.log(
            `Hey there! I am ${this.name} and I will be your ${this.teaches} professor.`
        )
    }
    grade_paper(paper){
        const grade = Math.floor(Math.random() * (5-1) + 1);
        console.log(grade);
    }
}
const andre = new Professors("Andre", "Chemistry");
andre.introduce_self();
andre.grade_paper("P4 Chemistry");
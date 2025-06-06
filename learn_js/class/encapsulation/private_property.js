#!/usr/bin/node

class Persons {

    name;

    constructor(name){
        this.name = name;
    }

    introduce_self(){
        console.log(`Hey there! I am ${this.name}`)
    }
}

class Student extends Persons{
    #year;

    constructor(name, year) {
        super(name)
        this.#year = year;
    }

    introduce_self(){
        console.log(`Hey there! I am ${this.name} and I'm in this ${this.#year} year`)
    }

    canStudyArchery(){
        if (this.#year > 1){
            return true;
        }
    }
}

const summer = new Student("Summer", 2)
summer.introduce_self();
console.log(summer.canStudyArchery());


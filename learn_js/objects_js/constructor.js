#!/usr/bin/node

function Cat(name, breed, color){
    this.name = name;
    this.breed = breed;
    this.color = color;
}

Cat.prototype.greeting = function(){
    console.log(`Hello, said ${this.name} the ${this.breed} ${this.color}`);
}

const cat_1 = new Cat("max", "Cymric", "white")
const cat_2 = new Cat("brue", "Cymric", "blue")

cat_2.greeting();
cat_1.greeting();

// Using Class
class NewCat {
    constructor(name, breed, color){
        this.name = name;
        this.breed = breed;
        this.color = color;
    }
    greeting(){
        console.log(`Hello, said ${this.name} the ${this.breed} ${this.color}`);
    }
}

my_cat_1 = new NewCat("alex", "Cymric", "green")
my_cat_2 = new NewCat("mic", "Cymric", "red")

my_cat_1.greeting();
my_cat_2.greeting();

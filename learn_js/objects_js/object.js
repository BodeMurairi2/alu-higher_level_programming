#!/usr/bin/node

function catGreeting() {
    console.log(`Hello, said ${this.name} the ${this.breed}.`);
}

const cat = {
    name: "Bertie",
    breed: "Cymric",
    color: "white",
    greeting: catGreeting
};

const cat2 = {
    name: "Milo",
    breed: "Siamese",
    color: "grey",
    greeting: catGreeting
};

cat.greeting();
cat2.greeting();

// store name inside catName variable
let catName = cat["name"]

// run greeting function
cat.greeting()

// update color to black
cat["color"] = "black"

console.log(`Cat name is ${cat.name}`)
console.log(`color is ${cat.color}`)

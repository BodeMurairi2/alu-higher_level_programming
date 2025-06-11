#!/usr/bin/node

class Example {
    somePublicMethod() {
        this.#somePrivateMethod();
    }

    #somePrivateMethod() {
        console.log("Call Me a Private Method");
    }
}

const myExample = new Example();

myExample.somePublicMethod();
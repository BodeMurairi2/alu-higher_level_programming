//1. display element
console.log(`Hello`);
console.log(`I like pizzas`);
//2. sending an alert onto the screen
//window.alert('This is an alert!');
//window.alert(`I like pizzas`);
// This is a comment

//3. getting an html element
//document.getElementById("myH1").textContent = 'Hello';
//document.getElementById('myP').textContent = 'I like pizzas!';

//4. variable
//a. number data type
let x;
let age = 25;
let price = 10.99;
let gpa = 3.95;

console.log(`You are ${age} years old`);
console.log(`The price is $${price}`)
console.log(`Your gpa is ${gpa}`)
// checking data type
console.log(typeof gpa)

// b. string data type
let firstName = "Bode";
console.log(typeof firstName);
console.log(`Your name is ${firstName}`);
let emailAddress = "bodemurairi2@gmail.com";
console.log(`Your email is ${emailAddress}`);

// c.Boolean
let online = true;
console.log(typeof online);
console.log(`${firstName} is ${online}`);

document.getElementById('myH1') = "Welcome";
document.getElementById('p1') = firstName;
document.getElementById('p2') = emailAddress;
document.getElementById('p3') = price;

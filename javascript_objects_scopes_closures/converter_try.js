#!/usr/bin/node

function converterBase1 (number, base) {
  if (number === 0) {
    const numberInNewBase = '0';
    console.log(numberInNewBase);
  } else {
    const listRest = [];
    while (number / base !== 0) {
      listRest.push(number % base);
      number = Math.floor(number / base);
    }
    const rest = [];
    for (let i = listRest.length - 1; i >= 0; i--) {
      rest.push(listRest[i]);
    }
    let numberInNewBase = '';
    for (const rests of rest) {
      numberInNewBase += rests;
    }
    return numberInNewBase;
  }
}

function converterBase2 (number, base) {
  if (number === 0) {
    console.log('0');
  } else {
    const listRest = [];
    while (number > 0) {
      listRest.push(number % base);
      number = Math.floor(number / base);
    }

    const rest = [];
    for (let i = listRest.length - 1; i >= 0; i--) {
      rest.push(listRest[i]);
    }

    let numberInNewBase = '';
    for (const digit of rest) {
      numberInNewBase += digit;
    }

    return numberInNewBase;
  }
}

exports.converter = function (base){
    return +process.argv[2]).toString(+process.argv[3]);
}

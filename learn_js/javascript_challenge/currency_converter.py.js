function converter() {

    const input = require('sync-input');
    const currencies = {
        USD: 1.0,
        JPY: 113.5,
        EUR: 0.89,
        RUB: 74.36,
        GBP: 0.75,
        RWF: 9.86,
        NRA: 1200,
        SHL: 2900,
    }
    console.log("Welcome to Currency Converter!");
    while (true) {

        let choice = Number(input("What do you want to do?\n 1. Convert Currencies\n 2. Exit program\n"))
        if (choice === 1) {
            let currency_from = (input("What do you want to convert from: ")).toUpperCase();
            let currency_to = (input("What do you want to convert to: ")).toUpperCase();
            let amount = Number(input("Enter the amount: "));
            if (currencies[currency_from] && currencies[currency_to]) {
                var conv = (amount * currencies[currency_to]) / currencies[currency_from]
            } else {
                console.log("Currency not found!")
            }
            console.log(`Amount: ${conv}`)
        }
        else
        if (choice == 2) {
            console.log("Goodbye!")
            break
        } else {
            console.log("Invalid Choice, Try Again")
            continue
        }
    }
}

converter()
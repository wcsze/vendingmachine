class VendingMachine:
    def __init__(self):
        self.drinks = {
            "Drink1": 1,
            "Drink2": 2,
            "Drink3": 3,
            "Drink4": 4
        }

    def showDrinks(self):
        print("Drinks Menu")
        for drink, price in self.drinks.items():
            print(f"{drink} : {price}")
        return
    
    def purchaseDrink(self, drink, payAmount):
        if drink not in self.drinks:
            print("Drink not found")
            return
        price = self.drinks[drink]
        if price > payAmount:
            print("Insufficient balance")
            return 
        else:
            change = payAmount - price
            self.returnChange(change)
            print("Thank you")
            return 

    def returnChange(self, change):
        if(change == 0):
            print("No change");
            return
        else:
            notes = [50,20,10,5,1]
            print("Change:")
            for note in notes:
                noteCount = change // note
                if noteCount > 0:
                    print(f"Note ${note}: {noteCount}")
                    change %= note
            return

vm = VendingMachine()
flag = True
while(flag):
    vm.showDrinks()
    drink = input("Enter the name of drink you want to purchase:")
    payAmount = input("PayAmount:")
    vm.purchaseDrink(drink, int(payAmount))
    buyAgain = input("Wish to buy again?Y/N:")
    if(buyAgain == "N"):
        flag = False

    
    

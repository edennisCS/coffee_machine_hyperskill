from time import sleep
water = 1200
milk = 540
beans = 120
coffee_cups = 9
money = 550

machine = ["The coffee machine has:",f"{water} of water",f"{milk} of milk",f"{beans} of coffee beans",f"{coffee_cups} of disposable cups",f"{money} of money"] 

for i in machine:
    print(i)
    sleep(0.5)

action = input("\nWrite action (buy, fill, take): ")
if action == "buy":
    purchase = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")
    if purchase == "1":
        money += 4
        water -= 250
        beans -= 16
        coffee_cups -= 1
    elif purchase == "2":
        money += 7
        water -= 350
        milk -= 75
        beans -= 20
        coffee_cups -= 1
    elif purchase == "3":
        money += 6
        water -= 200
        milk -= 100
        beans -= 12
        coffee_cups -= 1
        
elif action == "fill":
    add_water = int(input("Write how many ml of water do you want to add: "))
    add_milk = int(input("Write how many ml of milk do you want to add: "))
    add_beans = int(input("Write how many grams of coffee beans do you want to add: "))
    add_cups = int(input("Write how many disposable cups of coffee do you want to add: "))
    water += add_water
    milk += add_milk
    beans += add_beans
    coffee_cups += add_cups
    
    
elif action == "take":
    print(f"I gave you ${money}")
    money = 0

print("")
machine = ["The coffee machine has:",f"{water} of water",f"{milk} of milk",f"{beans} of coffee beans",f"{coffee_cups} of disposable cups",f"{money} of money"] 
for i in machine:
    print(i)
    sleep(0.5)

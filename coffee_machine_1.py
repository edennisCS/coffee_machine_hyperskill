water = int(input("Write how many ml of water the coffee machine has: "))
milk = int(input("Write how many ml of milk the coffee machine has "))
beans = int(input("Write how many grams of coffee beans the coffee machine has: "))
coffee_cups = int(input("Write how many cups of coffee you will need: "))

water_amount= 200
milk_amount=50
beans_amount = 15

available_water = (water/water_amount)
available_milk = (milk/milk_amount)
available_beans = (beans/beans_amount)

if available_water < coffee_cups or available_milk < coffee_cups or available_beans < coffee_cups:
        for i in range(coffee_cups, -1, -1):
            if not(available_water < i or available_milk < i or available_beans < i):
                print(f"No, I can make only {i} cups of coffee")
                break
else:
    if int(available_water) > coffee_cups and int(available_milk) > coffee_cups and int(available_beans) > coffee_cups:
            count= coffee_cups
            while True:
                    count +=1
                    if not(int(available_water) > count and int(available_milk) > count and int(available_beans) > count):
                            print(f"Yes, I can make that amount of coffee (and even {count - 1} more than that)")
                            break
    else:
        print("Yes, I can make that amount of coffee")

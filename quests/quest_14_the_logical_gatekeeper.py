# Level 3 - Quest 14
age = int(input("How old are you? "))
gold = int(input("How many gold coins do you have? "))

if age < 18 and gold < 20:
    print("Sorry, you are still young and short on coins you can't enter ):")
else:
    print("Congratulations! You fulfill all the requirements, you can enter")
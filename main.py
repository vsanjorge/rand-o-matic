from random import choice # importing random.choice

entrada = input("Please introduce a list of comma separated values (pizza,burger,salad,...)") # getting user input as string
lista = list(entrada.split(",")) # splitting the string into a list

print("\nRand-o-matic has chosen: " + (choice(lista))) # getting a random value from the list
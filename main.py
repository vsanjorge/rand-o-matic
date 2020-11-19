from random import choice # importing random.choice

entrada = input("Please introduce a list of comma separated values (pizza,burger,salad,...):\n") # getting user input as string
lista = list(entrada.split(",")) # splitting the string into a list

print("\nRAND-O-MATIC has chosen: " + (choice(lista))) # getting a random value from the list
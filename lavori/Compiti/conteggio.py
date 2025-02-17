frase = input("inserisci una frase: ")

occorrenze = {} 

for let in frase:
    occorrenze[let] = occorrenze.get(let, 0) + 1
    print(occorrenze)
#Aufgabe symmetrische differenz 1
list1 = [10, 21, 45, 66, 78]
list2 = [10, 22, 46, 66, 78, 90]
sym_difference = set(list1)^ set(list2)
diff = set(list1).symmetric_difference(list2)
print(diff)
print(sym_difference)
print()

#Aufgabe 2 common values
common_values = set(list1).intersection(list2)
common = set(list1) & set(list2)
print(common_values)
print(common)
print()

#Aufgabe 3 Hotel marios VS Hotel hilten
#Frage 1
marrios = {
    "name" : "Marrios", 
    "age"  :1999, 
    "payment_options" : ["card", "cash", "online"], 
    "available_rooms" : [800, 801, 802, 805, 900, 1000, 1001], 
    "price_per_night" :90, 
    "employees" : ["carlo", "maria", "marta", "luis", "fernando"]
}

hilten = {
    "name" : "Hilten", 
    "age" :1992, 
    "payment_options" : ["card","online"] ,
    "available_rooms" : [100, 800, 801, 805, 1000, 1001], 
    "price_per_night" : 70, 
    "employees" : ["artur", "maria", "oliver", "xenia", "fernando"], 

}

cost_marrios = int(marrios["price_per_night"] * 5)
cost_hilten = int(hilten["price_per_night"] * 5)
print(f"Fünf Übernachtungen kosten {cost_marrios} € im Hotel Marrios und {cost_hilten}  € im Hotel Hilten. Der Preisunterschied ist  {abs(cost_hilten - cost_marrios)} €.")
print()

#Frage 2

print(f'Guten Tag,  könnten Sie mir bitte eines der folgenden Zimmer reservieren: {marrios["available_rooms"]}  ? Danke.')
print(f'Guten Tag, könnten Sie mir bitte eines der folgenden Zimmer reservieren: {hilten["available_rooms"]} ? Danke.')
print(set(marrios["available_rooms"]).intersection(set(hilten["available_rooms"])))
print()
#Frage 3
print("Im Hotel Marrios gibt es:", len(marrios["payment_options"]), " und im Hotel Hilten gibt es:", len(hilten["payment_options"]),  "Zahlungsmöglichkeiten.")
print()
unterschied = set(marrios["payment_options"]) ^ set(hilten["payment_options"])
#diff = set(marrios["payment_options"]).symmetric_difference(hilten["payment_options"])
print(f'Die Hotels unterscheiden sich in den folgenden Zahlungsmöglichkeiten: {", ".join(unterschied)} ')  
#print(diff)
print()


if "fernando" in hilten["employees"]:
    print(f'er arbeitet im hotel : {hilten["name"]}')
    
if "fernando" in marrios["employees"]:
   
    print(f'Fernando arbeitet im hotel  {marrios["name"]} und ich werde dort übernachten')
else:
    print(f'Fernando arbeitet nicht hier')


#Bonusaufgabe



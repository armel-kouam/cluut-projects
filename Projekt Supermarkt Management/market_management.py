import pandas as pd
from supermarkt import *
from collections import Counter
# Aufgabe 4: Mitarbeiter und Produkte aus altem System einlesen
# Wechsle nun in deine Datei market_management.py - wir starten nun das Management unseres Supermarktes!
# Wir wollen Mitarbeiter und Produkte aus zwei CSV Dateien einlesen und zu unserem Supermarkt hinzufügen.
# Lese daher die Datei products.csv ein und speichere die Produkt-Zeilen als Tuple in der Liste products. 
# Lese außerdem die Datei employees.csv ein und speichere die Mitarbeiter-Zeilen als Tuple in der Liste employees.
product = pd.read_csv("products.csv", sep =";") #def __init__(self,  name, prod_id, category, price)
# print(product)
# print(product.info())
                                    # column_names = ["C", "A", "B"]Prod_id;Name;Category;PRICE
                                    # df = df.reindex(columns=column_names)
column_name = ["Name", "Prod_id", "Category", "PRICE"]
product_list = product[column_name]
# print(product_list)

product_tup = product_list.to_records(index=False)
print(product_tup)

print()
    
employee = pd.read_csv("employees.csv", sep =";") #  def __init__(self, name, age, pers_id, job)Pers_id;Name;JOB_ID;Age
# print(employee)
# print(employee.info())

column_names = ["Name", "Age", "Pers_id", "JOB_ID"]
employee_list = employee.reindex(columns=column_names)
# print(employee_list)

employee_tup = employee_list.to_records(index=False)
print(employee_tup)

# Vorsicht: Passe auf die Spaltennamen in den Dateien auf - es handelt sich hier um einen Export aus einem alten SAP Programm!
# Solltest du Probleme haben hier eine Lösung zu finden, schaue dir diese Seite an: https://www.kite.com/python/answers/how-to-reorder-columns-in-a-pandas-dataframe-in-python

print()

# Aufgabe 5: Supermarkt mit Mitarbeitern und Produkten erstellen
# Erstelle einen Supermarkt my_supermarket mit den Werten "Supermarkt Deluxe", "Marienplatz 1", "München".

my_supermarket = Supermarket("Supermarkt Deluxe", "Marienplatz 1", "München")
print(type(my_supermarket))

# Nimm deine employees und products und erstelle aus jedem Tupel ein Objekt.
# Für Elemente der employees Liste erstellst du Employee-Objekte und speicherst diese dann gesammelt in deinem Supermarkt.
# Für Elemente der products Liste erstellst du Products-Objekte und speichers diese dann gesammelt in deinem Supermarkt.

my_supermarket.employees = [Employee(*elem) for elem in employee_tup]
my_supermarket.products = [Product(*ele) for ele in product_tup]
# Dein Supermarkt soll am Schluss alle Attribute gesetzt haben - keine leeren Listen mehr!
# print(my_supermarket.products)

# Aufgabe 6: Supermarkt Management
# Verschaffe dir einen Überblick über deinen Supermarkt und beantworte die folgenden Fragen.
# P.S.: Wir lieben aussagekräftige Antwortsätze - f-String!! ;)
# Überlege dir für welche der Anfragen es ggf. Sinn macht in Zukunft eine neue Methode in einer der Klassen zu implementieren.
print()
            # max_ausgabe = ausgabe_sum[ausgabe_sum["Out"] == ausgabe_sum["Out"].max()].index.values[0]
# Wie viele Mitarbeiter hast du aktuell?

mitarbeiter = len(my_supermarket.employees)
print(f'Der Supermarkt "{my_supermarket.name}" hat {mitarbeiter} Mitarbeiter aktuell.')

# Was ist das teuerste Produkt in deinem Supermarkt?

max_price = max(my_supermarket.products , key=lambda x: x.price)
print (max_price.name, max_price.price)
print()
# Wie viel kostet ein Produkt im Durchschnitt in deinem Supermarkt?
list_price = [product.price for product in my_supermarket.products]
total_price = sum(list_price)
prod_total = len(my_supermarket.products)
prod_durch = total_price/prod_total
print(f'Ein Produkt kostet im Durchschnitt: {round(prod_durch,2)} €')

# Wie viele Produkte hast du für jede Kategorie?
categ = [prod.category for prod in my_supermarket.products]
categ_count = Counter(categ)
print(f'die Produkte und Kategorie sind: {categ_count}')
# Wie heißt der älteste Mitarbeiter?
max_age = max(my_supermarket.employees , key=lambda x: x.age)
print (f'Der/Die älteste Mitarbeiter(in) heißt: {max_age.name}, und er/sie ist {max_age.age} Jahre alt. Er/sie arbeitet als {max_age.job}.')
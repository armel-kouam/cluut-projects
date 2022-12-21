# Aufgabe 0: File Struktur für das Projekt
# Wir werden in diesem Projekt zwei Pythonfiles benötigen: 
# supermarket.py: Enthält die Klassen, die wir für unseren Supermarkt benötigen.
# market_management.py: Benutzt supermarket.py und wird für die Bearbeitung von Aufgabe 4-6 benut
from datetime import datetime
# Aufgabe 1: Die Supermarkt Klasse
# Erstelle zunächst eine Klasse Supermarket, mit den Attributen name (str), street (str), city (str).
# Jeder Supermarkt soll auch die Attribute employees und products haben, die zunächst als leere Liste implementiert werden sollen.
class Supermarket:
    def __init__(self, name, street, city):
        self.name = str(name)
        self.street = str(street)
        self.city = str(city)
        self.employees = []
        self.products = []
        
    

# Aufgabe 2: Die Mitarbeiter Klasse
# Erstelle eine Klasse Employee mit den Attributen name (str), age (int), pers_id (int), job (str).
class Employee:
    
    def __init__(self, name, age, pers_id, job):
        self.name = str(name)
        self.age = int(age)
        self.pers_id = int(pers_id)
        self.job = str(job)
        
        
    def greet_customer(self): 
       
        jetzt = datetime.now()
        uhr = jetzt.strftime("%H:%M")
        print(f"Guten Tag. Mein Name ist {self.name} und ich bin {self.job} in diesem Supermarkt. Es ist momentan {uhr} Uhr - wie kann ich Ihnen helfen?")
    
    
    def celebrate_birthday(self):
         self.age +=1
         print(f"Juhu! Heute werde ich {self.age} Jahre!")
     
# Jeder Mitarbeiter soll sich höflich den Kunden deines Supermarket vorstellen und einmal im Jahr seinen Geburtstag feiern können.
# Implementiere daher 2 Methoden, greet_customer und celebrate_birthday, die folgende Funktionen haben:
# greet_customer: Gibt folgenden Text aus: "Guten Tag. Mein Name ist __ und ich bin ___ Jahre in diesem Supermarkt. Es ist momentan __ Uhr - wie kann ich Ihnen helfen?"
# celebrate_birthday: Inkrementiert das Alter des Mitarbeiters und gibt den Text "Juhu! Heute werde ich _ Jahre!" aus.


# Aufgabe 3: Die Produkt Klasse
# Erstelle eine Klasse Product mit den Attributen name (str), prod_id (int), category (str), price (float).
# Jedes Produkt gehört in eine der folgenden Kategorien: food, drinks, others
# Überprüfe schon beim Erstellen eines neuen Objekts, ob die Kategorie richtig gesetzt ist. 
# Falls eine falsche Eingabe bei der Objekterstellung gemacht wurde, wähle stets die Kategorie others.
# Implementiere eine Methode apply_discount, die den Parameter discount (float) hat und eine Prozentzahl entgegennimmt.
# Teste in der Methode, ob discount zwischen 0 und 100 ist und wende den discount auf den Preis des Produkts an.
# Sollte ein fehlerhafter discount eingegeben worden sein, printe eine Warnung und berechne einen 5%-Rabatt.

class Product:
    def __init__(self,  name, prod_id, category, price):
        self.name = str(name)
        self.prod_id = int(prod_id)
        if category in ["food", "drinks"]:
            self.category = str(category)
        else:
            self.category = "other"
        self.price = float(price)
        
# Implementiere eine Methode apply_discount, die den Parameter discount (float) hat und eine Prozentzahl entgegennimmt.
# Teste in der Methode, ob discount zwischen 0 und 100 ist und wende den discount auf den Preis des Produkts an.
# Sollte ein fehlerhafter discount eingegeben worden sein, printe eine Warnung und berechne einen 5%-Rabatt.
        
    def apply_discount(self, discount):
        self.discount = float(discount)
        if 0 < self.discount < 100:
            self.price = self.price - (self.price * self.discount/100)
        else:
            print(f'Falsch discount eingegeben, wir werden mit 5%-Rabatt berechnen.')
            self.price = self.price - (self.price * 0.05)
            
    

    

# Aufgabe 4: Mitarbeiter und Produkte aus altem System einlesen
# Wechsle nun in deine Datei market_management.py - wir starten nun das Management unseres Supermarktes!
# Wir wollen Mitarbeiter und Produkte aus zwei CSV Dateien einlesen und zu unserem Supermarkt hinzufügen.
# Lese daher die Datei products.csv ein und speichere die Produkt-Zeilen als Tuple in der Liste products. 
# Lese außerdem die Datei employees.csv ein und speichere die Mitarbeiter-Zeilen als Tuple in der Liste employees.


# Vorsicht: Passe auf die Spaltennamen in den Dateien auf - es handelt sich hier um einen Export aus einem alten SAP Programm!
# Solltest du Probleme haben hier eine Lösung zu finden, schaue dir diese Seite an: https://www.kite.com/python/answers/how-to-reorder-columns-in-a-pandas-dataframe-in-python


# Aufgabe 5: Supermarkt mit Mitarbeitern und Produkten erstellen
# Erstelle einen Supermarkt my_supermarket mit den Werten "Supermarkt Deluxe", "Marienplatz 1", "München".


# Nimm deine employees und products und erstelle aus jedem Tupel ein Objekt.
# Für Elemente der employees Liste erstellst du Employee-Objekte und speicherst diese dann gesammelt in deinem Supermarkt.
# Für Elemente der products Liste erstellst du Products-Objekte und speichers diese dann gesammelt in deinem Supermarkt.


# Dein Supermarkt soll am Schluss alle Attribute gesetzt haben - keine leeren Listen mehr!


# Aufgabe 6: Supermarkt Management
# Verschaffe dir einen Überblick über deinen Supermarkt und beantworte die folgenden Fragen.
# P.S.: Wir lieben aussagekräftige Antwortsätze - f-String!! ;)
# Überlege dir für welche der Anfragen es ggf. Sinn macht in Zukunft eine neue Methode in einer der Klassen zu implementieren.


# Wie viele Mitarbeiter hast du aktuell?
# Was ist das teuerste Produkt in deinem Supermarkt?
# Wie viel kostet ein Produkt im Durchschnitt in deinem Supermarkt?
# Wie viele Produkte hast du für jede Kategorie?
# Wie heißt der älteste Mitarbeiter?
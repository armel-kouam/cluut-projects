import pandas as pd

print("Aufgabe 1 Budget Daten verstehen und einlesen")

budget_buch = pd.read_csv("budget.csv", sep =";")
print(budget_buch)

print()

print("Überblick über das DataFrame")
print(budget_buch.info())  

print()

print("Aufgabe 2 Gesamt Summe für Einnahmen und Ausgaben")
#hier mache ich Selection by label
summe_einnahme = budget_buch["In"].sum()
print(f'Die Summe Einnahmen ist: {summe_einnahme}')

summe_ausgabe = budget_buch["Out"].sum()
print(f'Die Summe Ausgaben ist: {summe_ausgabe}')

spar_box = abs(summe_einnahme - summe_ausgabe)
print(f' Mario und Julia konnten in den letzten Monaten: {round(spar_box,2)} sparen und zur Seite legen')

print("")
print("Aufgabe 3 Ausgabe pro Kategorie")
#print(budget_buch[["Out","Category"]])
#ausgabe = budget_buch[["Category","Out"]].groupby("Category").mean()
#print(ausgabe)

ausgabe_sum = budget_buch[["Category","Out"]].groupby("Category").sum()
print(ausgabe_sum)
print()
#ausgabe_sum.iloc[ausgabe_sum[‘Out’].idxmax()]


max_ausgabe = ausgabe_sum[ausgabe_sum["Out"] == ausgabe_sum["Out"].max()].index.values[0]
# Wofür geben Mario und Julia am meisten Geld aus?
print(f'Mario und Julia geben am meisten Geld für: {max_ausgabe} aus')

print()
print("Aufgabe 4 Visualisiere die Ausgaben pro Kategorie")
import seaborn as sns
sns.set_theme()
ausgabe_sns = sns.barplot(data = ausgabe_sum[ausgabe_sum["Out"] > 0], x = "Out", y = ausgabe_sum[ausgabe_sum["Out"] > 0].index)
ausgabe_sns.set_title("Ausgaben pro Kategorie")
ausgabe_sns.set_xlabel("Höhe der Ausgaben")
ausgabe_sns.set_ylabel("Kategorie")
ausgabe_sns.get_figure().savefig("expenses_per_category.png", bbox_inches='tight')
ausgabe_sns.figure.clf()

print()
print("BonusAufgabe: Ausgabe pro Monat")

budget_buch["Date"] = pd.to_datetime(budget_buch["Date"], format='%Y-%m-%d')
monat_ausgabe = budget_buch[["Date","Out"]].groupby(pd.Grouper(key="Date")).sum()
print(monat_ausgabe)

sns.set_theme()
monat_sns = sns.barplot(data = monat_ausgabe , y = "Out", x = monat_ausgabe.index.month_name(), errorbar=None)
ausgabe_sns.set_title("Ausgaben pro Monat")
ausgabe_sns.set_xlabel("Monatsnamen")
monat_sns.set_ylabel("Ausgaben")
monat_sns.get_figure().savefig("expenses_per_monat.png", bbox_inches='tight')
monat_sns.figure.clf()


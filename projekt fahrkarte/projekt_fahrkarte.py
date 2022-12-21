import json
with open ("tickets.json", "r") as file:
    ticket = json.load(file)
print(ticket)
print()

# x = 0
# # fahrkarte = len(ticket["tickets"])
# # for x in range(fahrkarte):
# #     print(f'für {ticket["tickets"][x]["name"]}, Wählen Sie bitte die {x}')
    
for x, t in enumerate(ticket["tickets"]):
    print(x, t["name"])
    
print()

choise_str = input("Bitte geben Sie ihre ausgewählte Nummer ein: ")
if not choise_str.isdigit():
    print(f'Die ausgewählte Nummer ist ungünstig.')
    exit()
choise = int(choise_str)
if choise < 0 or choise >= len(ticket["tickets"]) : 
    print(f'Die ausgewählte Nummer ist ungünstig.')
    exit()
else:
    print(f'Das Ticket : {ticket["tickets"][choise]["name"]}, kostet : {ticket["tickets"][choise]["price"]}€')
print()
#for geld in ticket["accepted_cash"]:
print(f'Der Automat akeptiert : {",".join([str(x) for x in ticket["accepted_cash"]])} €')

print()
ticket_price = ticket["tickets"][choise]["price"]
zu_bezahlen = 0
while zu_bezahlen < ticket_price :
    n_bezahlen = ticket_price - zu_bezahlen
    print(f" Es fehlt noch: {n_bezahlen} €")
    summe = int(input('Werfen Sie das Geld im Automat ein:' ))
    if  summe in ticket["accepted_cash"] :
        print (f'Sie haben, {summe} € eingeworfen')
        zu_bezahlen += summe #(bedeutet auch zu_bezahlen = zu_bezahlen + summe )
   
    else:
        print(f'Der Automat akzeptiert nicht dieses Geld')
        
        
if zu_bezahlen > ticket_price:
    rest = zu_bezahlen - ticket_price
    print(f"Sie bekommen {rest} € zurück")
       
print(f'Danke und gute Reise')
    

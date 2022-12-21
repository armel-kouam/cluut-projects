# Aufgabe 0: Log Analyse und Apache verstehen
# Unter dem Begriff Logging verstehen wir die Aufzeichnung von Fehlern und Ereignissen von Software.
# Jede Software, die du benutzt, hat eine Logging-Systematik implementiert, die dir bei der Fehlersuche hilft, wenn etwas mal nicht funktioniert.
# Fehlermeldungen und Ereignisse werden meistens in eine oder mehrere Dateien geschrieben, sogenannte Log Files.
# In der folgenden Aufgabe werden wir uns genau so ein Log File anschauen und es analysieren.
# Bevor wir loslegen, starte eine kurze Recherche und beantworte folgende Fragen:
# Was ist ein Apache HTTP Server?
print("Apache ist ein beliebter Open-Source, plattformübergreifender Webserver, der nach den Zahlen der beliebteste Webserver überhaupt ist")
# Welches Format haben Apache Access Logs?
# Welche Informationen sind in einer Access Log Zeile enthalten?
# Tip 1: https://en.wikipedia.org/wiki/Apache_HTTP_Server#Feature_overview
# Tip 2: https://httpd.apache.org/docs/2.2/logs.html#common%20
# Tip 3: https://www.sumologic.com/blog/apache-access-log/

# Aufgabe 1: Apache Logs analysieren
# Lade die zip-Datei herunter und speichere alle enthaltenen Files in einem Cloud9 Folder für dieses Projekt.
# Öffne die Datei apache_logs in einem Python Skript namens log_analysis.py und lese alle Zeilen in eine Liste ein.
# Schau dir die erste Zeile der Datei an und schreibe in einem Kommentar auf, welche Informationen wir in jeder Log Zeile haben.

print()
with open("apache_logs", "r") as file:
    log_files = file.readlines()
# print(log_files)
# print(log_files[0])
"Wir habe in der erste Zeile als Informationen: eine IP adress, (Datum, Uhr, GMT), Get, Http protocol, Browser(Mozilla,AppelWebkit,Chrome)"



# Aufgabe 2: HTTP Status Code des ersten Log Eintrags
# Speichere die erste Zeile des Log Files in eine separate Variable first_line.
# Splitte die Zeile in ihre Einzelteile mit dem split()-Befehl.
# Extrahiere nun den HTTP Status Code.
# Welcher Status Code wurde für diese Anfrage an den HTTP Server zurückgegeben?
# Was bedeutet der HTTP Status Code?

first_line = log_files[0]
# for line in first_line :
log_line = first_line.split()
print(log_line)
print(type(log_line))
print(log_line[8])
"WIr haben 200 (OK )als Status Code zurückbekommen d.h die Anfrage wurde korrekt und ohne Fehler ausgeführt"
# 100 – Continue
# 102 – Processing
# 200 – OK
# 301 – Moved Permanently
# 302 – Moved Temporarily
# 400 – Bad Request
# 404 – Not Found
# 410 – Gone
# 500 – Internal Server Error
# 503 – Service Unavailable

 
# Aufgabe 3: HTTP Status Code Analyse
# Analysiere nun alle Log Zeilen und speichere alle HTTP Status Codes in einer Liste mit dem Namen status_codes.
# Zähle, wie oft der Status Code 200 vorkommt und speichere den Wert in status_200.
# Zähle, wie oft der Status Code 404 vorkommt und speichere den Wert in status_404.
# Importiere nun die Klasse Counter aus dem Modul collections.
# https://docs.python.org/3/library/collections.html#collections.Counter
# Benutze die Counter Klasse, um für jeden Status Code in status_codes die Anzahl an Vorkommen zu bestimmen.
# Welche sind die 3 häufigsten HTTP Status Codes?

print(type(log_files))
status_codes =[]
for ht in log_files:
    codes = ht.split()[8]
    status_codes.append(codes)
    # print(status_codes)

status_codes = [ht.split()[8] for ht in log_files]
# print(status_codes)

from collections import Counter

count_code = Counter(status_codes)
# print(count_code)

status_200 = count_code["200"]
status_404 = count_code["404"]

# print(f"Der Status Code 200, kommt {status_200} vor")
# print(f"Der Status Code 404, kommt {status_404} vor")

am_haeufigsten = count_code.most_common(3)
# print(am_haeufigsten)





# Aufgabe 4: Fehlerbehebung auf dem HTTP Server
# Um deine Webapplikation für Benutzer zu verbessern, musst du herausfinden, welche Anfragen nicht funktioniert haben.
# Filtere deshalb die Log Zeilen nach dem Status Code 404 und speichere alle Zeilen, die diesen Status Code beinhalten, in der Liste lines_with_404.
# Benutze für das filtern die filter()-Funktion und lambda.
# Speichere in einer neuen Liste namens resource_list die angefragten URL Paths (resource requested).
# Benutze hier wieder die split()-Methode.
# Tip: https://www.sumologic.com/blog/apache-access-log/
# Wieviele verschiedene Fehlerquellen hast du gefunden?
# Welche sind die 3 häufigsten Fehlerquellen bei den Anfragen auf unseren Apache Server?
# Tip: https://docs.python.org/3/library/collections.html#collections.Counter

lines_with_404 = list(filter(lambda x : x.split()[8] == "404", log_files)) # "404" in x
# print(lines_with_404)

resource_list = [line_path.split()[6] for line_path in lines_with_404]
print(resource_list)

resourc_l = len(set(resource_list))
# print(resourc_l)

meistens = Counter(resource_list)#.most_common(3)
print(len(meistens))



# Bonus Aufgabe: Log Report
# Ziel der Aufgabe ist es einen Log Report zu erstellen, der zwei Abbildungen beinhaltet.
# Installiere hierfür das Python Modul fpdf mit pip: https://pypi.org/project/fpdf/
# Das Skript log_pdf.py aus dem LMS beinhaltet eine Klasse PDF, mit der du deinen Log Report erstellen kannst.
# Importiere die Klasse PDF aus dem Modul log_pdf in dein Skript.
# Erstelle ein Histogram mit seaborn für deine Liste status_codes und speichere den Plot in der Datei status_codes.png.
# Erstelle ein Histogram mit seaborn für deine Liste resource_list und speichere den Plot in der Datei resource_list.png.
# Erstelle eine Liste plots, die zwei Strings enthält: status_codes.png, resource_list.png
# Erstelle eine Instanz der Klasse PDF mit dem Namen log_report.
# Erstelle nun eine for-Schleife über die Elemente plot in deiner Liste plots und rufe in der for-Schleife den folgenden Befehl auf:
#      log_report.print_page(plot)
# Um den PDF Report nun zu erstellen, füge die folgende Zeile in deinen Code: 
#      log_report.output("LogReport.pdf", "F") 
# Schaue dir den PDF Report an. Was könnte noch verbessert werden?
import pandas as pd
from log_pdf import PDF
import seaborn as sns 
# Erstelle ein Histogram mit seaborn für deine Liste status_codes und speichere den Plot in der Datei status_codes.png.
sns.set_theme()
status_sns = sns.histplot(data = status_codes)
status_sns.set_title(" Liste status codes")
status_sns.get_figure().set_figwidth(6)
status_sns.get_figure().set_figheight(8)
status_sns.get_figure().savefig("status_codes.png", bbox_inches='tight')
status_sns.figure.clf()

# Erstelle ein Histogram mit seaborn für deine Liste resource_list und speichere den Plot in der Datei resource_list.png.
sns.set_theme()
resource_sns = sns.histplot(y = resource_list, binwidth=4)
resource_sns.set_title("Liste resource")
resource_sns.get_figure().set_figwidth(9)
resource_sns.get_figure().set_figheight(14)
resource_sns.get_figure().savefig("resource_list.png", bbox_inches='tight')
resource_sns.figure.clf()

# Erstelle eine Liste plots, die zwei Strings enthält: status_codes.png, resource_list.png
plots = ["status_codes.png", "resource_list.png"]
# Erstelle eine Instanz der Klasse PDF mit dem Namen log_report.
log_report = PDF()
for plot in plots:
    log_report.print_page(plot)
log_report.output("LogReport.pdf", "F") 
        
    
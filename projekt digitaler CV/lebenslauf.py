# In diesem Projekt werden wir uns das Feature "Website Hosting" von Amazon S3 zunutze machen und in S3 unseren digitalen Lebenslauf (CV) hosten.

# Diesen CV können wir dann jederzeit mit potenziellen Arbeitgebern teilen oder einfach als cooles, erstes Projekt benutzen, das wir in AWS gebaut und personalisiert haben.

# Neben den AWS Skills, die wir mit diesem Projekt stärken, werden wir auch einen kurzen Exkurs in die Welt des Web Developments machen. Wir schauen uns an, wie HTML funktioniert und werden einige Anpassungen in einem HTML File machen.

# Aufgabe 1: Bucket für das Webhosting
# Erstelle ein Bucket mit dem Namen my-digital-cv-VORNAME-NACHNAME-2022
# Unter Properties (Einstellungen) enable Static website hosting. Gib hier als Index document index.html an.
# Unter Permissions müssen wir nun Zugriff auf unser Bucket erlauben.
# Entferne hierfür das Häkchen unter Block public access (bucket settings)
# Füge die Bucket policy policy.json bei Bucket policy ein.
# Tausche in der Policy Zeile 12 aus, in der die Ressource definiert wird. Füge deinen Bucketnamen      zwischen ::: und /* ein.

# Die Policy erlaubt (Effect: Allow) allen (Principal: *) das Herunterladen (Action: s3:GetObject, s3:GetObjectVersion) deiner HTML Datei und ggf. zugehörigen Bildern (Ressource: DEIN BUCKET IDENTIFIER).
# Lade die Dateien index.html und avatar.png in den Hauptordner deines Buckets.
# Teste, ob du den Lebenslauf sehen kannst, in dem du unter Properties > Static website hosting auf die     angegebene URL klickst.
#

# Aufgabe 2: HTML Basics
# HTML steht für Hyper Text Markup Language und ist die Standardsprache um Webseiten zu erstellen.

# HTML ist keine typische Programmiersprache, so wie du sie bisher mit Python kennengerlent hast. Mit HTML beschreiben wir, wie eine Webseite aussehen soll, wohingegen wir in Python Befehle von einem Computer ausführen lassen.

# HTML besteht immer aus einer Reihe von Elementen, die dann von deinem Webbrowser entsprechend dargestellt werden. Elemente haben immer einen Starttag, Content und einen Endtag. 

# Das schaut immer so aus: 

# <tagname>Content steht zwischen den tags</tagname>
# Im File index.html findest du nun ein Template  für deinen CV.
# Suche die folgenden Tags im  index.html Dokument, schreibe dir die Zeilen auf, wo der Tag geöffnet und     geschlossen wird.
# Recherchiere außerdem online, wofür diese Tags stehen und warum wir sie in unserem CV brauchen.
# <html></html>: Beginn und Ende von einem HTLM Dokument
# <body></body>: Zwischen den Beide liegt der sichtbare Teil des HTML-Dokuments.
# <div></div> definiert die Teile 
# <h1></h1> : hier werden HTML-Überschriften definiert
# <img>: HTML-Bilder werden mit diesem Tag definiert.
# <p></p>:hier werden HTML-Absätze definiert

# Tipp: https://www.w3schools.com/html/html_basic.asp

# Aufgabe 3: CV Text anpassen 
# Öffne das index.html File in einem guten Editor mit Syntax Highlighting (z.b. VSCode, Notepad++) auf deinem Computer lokal oder einfach in Cloud9.

# Basis Informationen anpassen 
# Füge deinen Namen im CV ein.
# Gib deine Adresse, Email und Telefonnummer an. 
# Als Jobbezeichnung kannst du AWS Cloud Developer angeben.

# Skills anpassen  
# Suche dir 4 Skills raus, z.B. Python, AWS, DevOps, Scrum und trage sie in dem Paragraph Skills ein. Passe hier stets die Prozentzahl an - sie stellt dar, wie gut du in diesem Skill bereits bist.
# Tipp: Die Prozentzahl muss sowohl im Content als auch im style-Attribut angepasst werden.

# Sprachen anpassen
# Welche Sprachen sprichst du?  Passe den Bereich Languages entsprechend deiner Fähigkeiten an.

# Arbeitserfahrung eintragen
# Auf der rechten Seite des CVs kannst du über deine bisherigen Jobs berichten, die für die Stelle interessant sind, auf die du dich in Zukunft bewerben möchtest. Diese Informationen kannst du im Bereich Work Experience eintragen
# Tipp: Jede Work Experience ist in einem <div> Block gespeichert. Möchtest du mehr oder weniger      Punkte auflisten, kannst du einen <div>-Block duplizieren oder löschen.

# Deinen Bildungsweg anpassen  
# Wo bist du zur Schule oder Uni gegangen? Trage in den <div>-Blöcken unter Education deine Informationen ein.
# Aufgabe 4: Dein Bild einfügen
# Suche im index.html Dokument nun nach dem Tag <img.
# Welches Attribut in diesem Tag musst du anpassen, sodass du hier ein Bild von dir einfügen kannst?
# Lade ein Bild von dir in dein Amazon S3 Bucket und passe die entsprechende Stelle im index.html Dokument  so an, dass der HTML Code auf dein Bild zeigt.
# Tipp: https://www.w3schools.com/html/html_images.asp
 

# Aufgabe 5: CV checken, Fehler beheben und hochladen 
# Speichere das index.html File, wenn du alle Anpassungen gemacht hast und überprüfe die Lesbarkeit.    
         
# Solltest du lokal auf deinem Computer arbeiten, solltest du mit Doppelklick auf das File eine Vorschau     in deinem Browser bekommen. Lade die finale Version des index.html dann wieder in dein S3 Bucket.
 
# Arbeitest du in Cloud9, lade die überarbeitete Datei herunter und in S3 hoch. Klicke wieder auf den URL-Link unter Properties, um deinen CV zu sehen.
 

# Solltest du Unschönheiten sehen, versuche sie zunächst selbst zu beheben und tüftle mit dem HTML Code herum. Wenn du feststeckst und nicht weiterkommst, melde dich im     Slack Channel bei uns oder komm in die nächste Live Session, sodass wir gemeinsam einen Blick darauf werfen.


# Glückwunsch! Du hast deinen ersten eigenen digitalen CV erstellt!
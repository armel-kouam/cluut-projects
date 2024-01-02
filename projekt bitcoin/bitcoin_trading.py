from datetime import datetime
import requests
import json
import boto3
import pandas as pd
import seaborn as sns
from botocore.exceptions import ClientError

# current date und current time erstellen
jetzt = datetime.now()
current_date = jetzt.strftime("%d.%m.%y")
current_time = jetzt.strftime("%H:%M:%S")
print(current_date)
# print(current_time)

# Frage den aktuellen Bitcoin Preis über diesen API Endpoint ab
url_bit = "https://api.coindesk.com/v1/bpi/currentprice.json" 
reques = requests.get(url_bit)
bitcoin = reques.json()
bitcoin_price = bitcoin["bpi"]["USD"]["rate"]
print(bitcoin_price)

# Versuche nun in einem try-except Block die Datei bitcoin_prices.csv  aus dem S3 Bucket unter dem Prefix trading herunterzuladen. Verwende hier wie gewohnt boto3.
bucket_name = "cluut-aws-developer-kurs-armel-kouam-29-12-2022"
file_name = "bitcoin_prices.csv"
key = f"trading/{file_name}"
    
s3 = boto3.client('s3')
try:
    s3.download_file(bucket_name, key, file_name)
    
except ClientError as e:
    
    print("error 404 file existiert noch nicht")
    
finally:
    with open (file_name, "a") as file:
        file.write(f'{current_date};{current_time};{bitcoin_price}\n')


# Lade die CSV Datei wieder mit boto3 in das S3 Bucket hoch.
s3.upload_file(file_name, bucket_name, key)


# # Lese die CSV Datei bitcoin_prices.csv, die du jetzt auch lokal hast, mit pandas ein.
bitcoin_p = pd.read_csv(file_name, sep=";", header=None, thousands=",")
print(bitcoin_p)

# # Extrahiere alle Zeilen aus dem DataFrame, die zum heutigen Tag gehören.


# # # Erstelle mit seaborn einen lineplot, der die Preise auf der y-Achse und die Uhrzeit auf der x-Achse anzeigt.
sns.set_theme()
bitcoin_sns = sns.lineplot(data = bitcoin_p, x =bitcoin_p[1] , y =bitcoin_p[2] )
bitcoin_sns.set_title(f"Bitcoin Price von {current_date} ")
bitcoin_sns.set_xlabel("time")
bitcoin_sns.set_xticklabels(bitcoin_p[1], rotation = 45, horizontalalignment = 'right')
bitcoin_sns.set_ylabel("price")
# bitcoin_sns.get_figure().set_figwidth()
# bitcoin_sns.get_figure().set_figheight()
bitcoin_sns.get_figure().savefig(f"bitcoin_prices_{current_date}.png", bbox_inches='tight')
bitcoin_sns.figure.clf()

# # # Lade den Plot ebenfalls in das S3 Bucket cluut-aws-developer-kurs-DEIN-NAME-21-01-2022 unter das Prefix trading/plots/.

# # s3.upload_file(f"bitcoin_prices_{current_date}.png", bucket_name, f"trading/plots/bitcoin_prices_{current_date}.png")

s3.upload_file(f"bitcoin_prices_{current_date}.png", bucket_name, f'trading/plots/bitcoin_prices_{current_date}.png')

 
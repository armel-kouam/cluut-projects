import pandas as pd
import seaborn as sns
from textblob import TextBlob
import json
with open ("data.json", "r") as file:
    tweet = json.load(file)
#print(tweet)
print()
# new_name = list(filter(lambda x : len(x) <= 7, names))
# print(new_name)
print("Alle tweet mit dem Thema Obama")
obama_tweet = list(filter(lambda x : x["topic"] =="obama", tweet))
#print(obama_tweet)

for tweets in obama_tweet:
    sentiment_tweet=tweets["tweet"]
   # print(sentiment_tweet)
    testimonial = TextBlob(sentiment_tweet)
    polarity = testimonial.sentiment.polarity
    #print(polarity)
    if polarity < -0.2:
        tweets["sentiment"] = "negative"
    elif polarity > 0.2:
        tweets["sentiment"] = "positive"
    else:
        tweets["sentiment"] = "neutral"
    # print(tweets["sentiment"])
      
with open ("sentiment.json", "w") as file:
     json.dump(obama_tweet, file)
     
# sentiment_list =[]
# for tweet in obama_tweet:
#     sentiments = tweet["sentiment"]
#     sentiment_list.append(sentiments)
    
sentiment_list = [tweet["sentiment"] for tweet in obama_tweet]
print(sentiment_list)
sns.set_theme()
sentiment_sns = sns.histplot(data = sentiment_list)
sentiment_sns.patches[0].set_facecolor('salmon')
sentiment_sns.patches[1].set_facecolor('yellow')
sentiment_sns.patches[2].set_facecolor('green')
sentiment_sns.set_title("Sentiment")
sentiment_sns.get_figure().savefig("sentiments.png")
sentiment_sns.figure.clf()


import csv
import re
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer

obj = SentimentIntensityAnalyzer()
#encodings = ['utf-8', 'latin-1']
# code to extract text
text = []

with open('Dataset.csv','r',newline='',encoding='latin-1') as file :
        csv_reader = csv.DictReader(file)
    
        for row in csv_reader:
            text.append(row['Summary'])
print(text)
def remove_non_decodable(text):
    pattern = re.compile(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff]')
    return re.sub(pattern, '', text)
cleaned_text = [remove_non_decodable(t) for t in text]
#print(cleaned_text)

sentiments = []
for t in cleaned_text:
     sentiment = obj.polarity_scores(t)
     #sentiments.append(sentiment)
     if sentiment['compound'] >= 0.05:
        overall_sentiment = 'Positive'
     elif sentiment['compound'] <= -0.05:
        overall_sentiment = 'Negative'
     else:
        overall_sentiment = 'Neutral'
         
     
     print(f"Sentiment scores: {sentiment}")
     print(f"Overall sentiment: {overall_sentiment}\n")
     print(f"String: {t}")
#print(sentiments)


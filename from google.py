from google.colab import files
uploaded = files.upload()
 
import pandas as pd
 
df = pd.read_csv("Womens Clothing E-Commerce Reviews.csv")
 
df.head(10)
  
import numpy as np
import nltk
nltk.download('vader_lexicon')
 
from nltk.sentiment.vader import SentimentIntensityAnalyzer
 
sid = SentimentIntensityAnalyzer()
 
# replace missing values with empty strings
 
df[ 'Review Text'] = df['Review Text'].replace(np.nan, '',regex=True)
 
# iterate over the review text column and calculate the sentiment scores
 
sentiment_scores = []
 
for text in df['Review Text']:
 
   scores = sid.polarity_scores(text)
 
   sentiment_scores.append(scores['compound'])
 
df['Sentiment Score'] = sentiment_scores
 
def get_sentiment_label(score):
 
 if score >= 0.05:
 
   return 'Positive'
 
 elif score <= -0.05:
 
   return 'Negative'
 
 else:
 
   return 'Neutral'
 

sentiment_labels = df['Sentiment Score'].apply(get_sentiment_label)
 
df['sentiment_labels'] = sentiment_labels
 
df.head(10)
   
import matplotlib.pyplot as plt
 
#count the number of reviews for each sentiment label
 
sentiment_counts = df['sentiment_labels'].value_counts()
 
#create a pie chart
 
plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%')
plt.title('Sentiment Distribution')
plt.show()

import matplotlib.pyplot as plt
  
# group the data by rating and sentiment label, and count the number of reviews in each group
 
grouped = df.groupby(['Rating', 'sentiment_labels']).size().reset_index(name='Count')
 
# iterate over each rating and plot a pie chart of the sentiment label distribution
 
for rating in range(1, 6):
   data = grouped [grouped['Rating'] == rating]
   plt.pie(data['Count'], labels = data['sentiment_labels'], autopct='%1.1f%%')
   plt.title(f'Sentiment Label Distribution for Rating {rating}')
   plt.show()
 
import matplotlib.pyplot as plt
  
fig = plt.figure(figsize=(8,6))
 
df.groupby(['Rating', 'sentiment_labels']).size().unstack().plot(kind= "bar", stacked=True)
plt.title('Sentiment Label vs Rating')
plt.xlabel('Rating for Raisoni University Uniform')
plt.ylabel('Count')
plt.show()


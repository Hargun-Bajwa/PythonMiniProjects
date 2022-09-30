from textblob import TextBlob

text="You"
blob=TextBlob(text)
sentiment_polarity_score=blob.sentiment.polarity
print(sentiment_polarity_score)
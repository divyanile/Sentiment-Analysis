import re
import pandas as pd
from textblob import TextBlob

def get_tweets(): 
    #Import .csv file using pandas library
    try:
        column_list = ["ItemID", "Sentiment", "SentimentText"]
        tweets = pd.read_csv("dataset.csv", encoding='latin1', usecols=column_list)
        covertedTweets = tweets.values.tolist()
        
        return covertedTweets

    except:
        print("Error!" )

def clean_tweet(tweets):
    #Clean tweets for analysis
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweets).split())

def get_tweet_sentiment(tweets):
        # create TextBlob object of passed tweet text
        analysis = TextBlob(clean_tweet(tweets))
        
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        else:
            return 'negative'

def main():
    # calling function to get tweets
    tweets = get_tweets()

    #Empty Arrays to sort positive and negative tweets
    positivetweets = []
    negativetweets = []

    #Sorting Positive and Negative Tweets
    for i in range(len(tweets)): 
        if(get_tweet_sentiment(tweets[i][2]) == 'positive'): 
            positivetweets.append(tweets[i])
        else:
            negativetweets.append(tweets[i])

    # percentage of positive tweets
    print("Positive tweets percentage: {} %".format(100*len(positivetweets)/len(tweets)))
    
    # percentage of negative tweets
    print("Negative tweets percentage: {} %".format(100*len(negativetweets)/len(tweets)))
    
if __name__ == "__main__":
    # calling main function
    main()
'''
AIM:
To extract stock sentiment from news headlines using basic Natural Language Processing (NLP) techniques.

THEORY:
Stock sentiment analysis is a technique used in Natural Language Processing to determine whether a news headline expresses a positive, negative, or neutral opinion about stocks or the financial market.
This experiment uses a lexicon-based approach, where predefined sets of words are used to identify sentiment:
- Positive words (e.g., gain, profit, rise) indicate favorable market conditions
- Negative words (e.g., loss, fall, decline) indicate unfavorable conditions

The sentiment score is calculated using the formula:
Sentiment Score = Number of Positive Words − Number of Negative Words

Based on the score:
If Score > 0 → Positive Sentiment
If Score < 0 → Negative Sentiment
If Score = 0 → Neutral Sentiment
This method is simple and efficient for basic sentiment classification tasks.

ALGORITHM:
1. Input a list of stock news headlines.
2. Convert each headline to lowercase.
3. Tokenize the headline into individual words.
4. Define lists of positive and negative words.
5. Count the number of positive and negative words in each headline.
6. Calculate the sentiment score.
7. Classify the sentiment based on the score.
8. Display the headline along with its sentiment.
'''
#Sample headlines

headlines = [
    "Stocks gain as economy shows signs of recovery",
    "Company reports loss and faces investor concerns",
    "Market remains stable despite global uncertainties"
]

#Define sentiment words
positive_words = {"gain", "profit", "rise", "recovery", "stable"}
negative_words = {"loss", "fall", "decline", "concerns", "uncertainties"}

#Analyyzing sentiment

def analyze_sentiment(headline):
    words = headline.lower().split()

    pos_count = sum(1 for w in words if w in positive_words)
    neg_count = sum(1 for w in words if w in negative_words)

    score = pos_count - neg_count

    if score>0:
        return "Positive"
    elif score<0:
        return "Negative"
    else:
        return "Neutral"
    
for h in headlines:
    print("Headline : ",h)
    print("Sentiment : ",analyze_sentiment(h))
    print()
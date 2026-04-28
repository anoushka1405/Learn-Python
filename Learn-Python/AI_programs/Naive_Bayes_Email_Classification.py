'''
To demonstrate how probabilistic reasoning can be used to classify emails as spam or not spam using Bayes’ Theorem.

Bayes’ Theorem is a statistical method used to calculate the probability of an event based on prior knowledge of conditions related to the event. In spam classification, it helps determine whether an email is spam or not based on the words present in it.
The formula of Bayes’ Theorem is:

P(Spam | Words) = [P(Words | Spam) × P(Spam)] / P(Words)
Where:P(Spam | Words) is the probability that the email is spam given the words.
P(Words | Spam) is the probability of words appearing in spam emails.
P(Spam) is the prior probability of spam emails.
P(Words) is the probability of words appearing in all emails.

Naïve Bayes assumes that all words are independent of each other.

ALGORITHM:
1. Collect a dataset of emails labeled as spam and not spam.
2. Preprocess the emails by converting text to lowercase and splitting into words.
3. Calculate prior probabilities:P(Spam) and P(Not Spam).
4. Calculate likelihood probabilities for each word:P(word | Spam) and P(word | Not Spam).
5. Apply Laplace smoothing to avoid zero probability.
6. For a new email, calculate:Score(Spam) and Score(Not Spam).
7. Compare both scores:
If Score(Spam) > Score(Not Spam), classify as Spam.
Otherwise, classify as Not Spam.

'''

from collections import defaultdict
import math

# Training data
emails = [
    ("win money now", "spam"),
    ("limited offer win cash", "spam"),
    ("meeting at 10am", "ham"),
    ("project discussion", "ham")
]

#Counting Words
spam_words = defaultdict(int)
ham_words = defaultdict(int)
spam_count = ham_count = 0

for text,label in emails:
    words = text.split()
    if label=="spam":
        spam_count+=1
        for w in words:
            spam_words[w]+=1
    else:
        ham_count+=1
        for w in words:
            ham_words[w]+=1

vocab = set(list(spam_words.keys())+list(ham_words.keys()))
V = len(vocab)

def classify_emails(email):
    words = email.split()

    p_spam = math.log(spam_count/len(emails))
    p_ham = math.log(ham_count/len(emails))

    for w in words:
        p_spam += math.log((spam_words[w] + 1) / (sum(spam_words.values()) + V))
        p_ham += math.log((ham_words[w] + 1) / (sum(ham_words.values()) + V))

    return "spam" if p_spam>p_ham else "not spam"
    

print(classify_emails("win cash now"))
'''
Keyphrase extraction is a technique in Natural Language Processing (NLP) used to automatically identify important words or phrases from a document. In scientific articles, keyphrases help summarize the main topics and improve information retrieval.
There are two main approaches:
- Statistical methods (like Term Frequency)
- Linguistic methods (like part-of-speech tagging)

In this experiment, we use a simple frequency-based approach:
Words that appear more frequently (excluding common stopwords) are considered more important.

Term Frequency (TF) Formula:
TF(word) = Number of times the word appears / Total number of words

ALGORITHM:
1. Input a scientific article (text).
2. Convert text to lowercase.
3. Remove punctuation and special characters.
4. Tokenize text into words.
5. Remove stopwords.
6. Count frequency of each word.
7. Sort words based on frequency.
8. Select top N words as keyphrases.
9. Display the extracted keyphrases.

'''

from collections import Counter
import string

# Sample scientific text
text = """
Machine learning is a field of artificial intelligence that focuses on training algorithms
to learn from data. It is widely used in scientific research for prediction, classification,
and data analysis. Machine learning models improve automatically through experience.
"""

#List of common stopwords
stopwords = {"the", "is", "in", "and", "to", "of", "that", "for", "a", "with", "as", "on", "by", "an", "are"}

#Preprocessing
text = text.lower()

for p in string.punctuation:
    text = text.replace(p, "")

words = text.split()
filtered_words = [w for w in words if w not in stopwords]

freq = Counter(filtered_words)
top_n = 5
keyphrases = freq.most_common(top_n)

#Output
print("Extracted Keyphrases:")

for word,count in keyphrases:
    print(word," : ",count)
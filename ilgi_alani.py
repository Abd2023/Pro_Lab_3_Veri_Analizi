from collections import Counter
import re




def find_interests(tweets):
    words = []
    for tweet in tweets:
        words.extend(re.findall(r'\b\w+\b', tweet))
    common_words = Counter(words)
    return common_words.most_common(10)

# Suppose 'user' is a User object


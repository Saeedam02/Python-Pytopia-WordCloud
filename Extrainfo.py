from wordcloud import STOPWORDS
from wordcloud import wordcloud
print(STOPWORDS)
# These words are used frequently in English language and in wordcloud computations, they won't be used as a word.
# But if we want to show them as well, we can change the wordcloud class attribution stopwords from None to [].
# If we use STOPWORDS=['the',] it will ignore the and show others.
# Also we can use stopwords = STOPWORDS.union({'love',}) and it will put love into stopwords.

stop_words=set(['and','or']) # set of words that won't be considered in our analysis
wordcloud.to_file('wordcloud.png') # Convert a wordcloud object into a png file.
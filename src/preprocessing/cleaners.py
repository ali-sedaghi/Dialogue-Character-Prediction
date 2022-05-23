import re
import nltk
from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import stopwords


nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
tokenizer = TreebankWordTokenizer()


def my_tokenize(string):
    return tokenizer.tokenize(string)


def remove_whitespaces(string):
    string = string.replace('\n', ' ').replace('\t', ' ')
    string = re.sub(' +', ' ', string)
    return string


def to_lower_case(string):
    return string.lower()


def remove_special_chars(string):
    s = re.sub('@[^ ]*', '', string)
    return re.sub('[^a-z\s]+', '', s)


def remove_short_words(string):
    tokens = my_tokenize(string)
    new_string = ''
    for token in tokens:
        if len(token) >= 3:
            new_string += token + ' '
    return new_string[:-1]


def remove_stopwords(string):
    tokens = my_tokenize(string)
    new_string = ''
    for token in tokens:
        if not (token in stop_words):
            new_string += token + ' '
    return new_string[:-1]

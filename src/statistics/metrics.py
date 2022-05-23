import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud


def generate_word_cloud(corpus, person):
    word_cloud = WordCloud(
        width=720, height=720,
        background_color='white',
        min_font_size=10
    ).generate(corpus)
    plt.figure(figsize=(16, 16), facecolor=None)
    plt.imshow(word_cloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.savefig(f'../../statistics/{person}_word_cloud.png')


def generate_histogram(corpus, person, counts=20):
    my_dict = Counter(corpus.split())
    my_list = [(k, v) for k, v in sorted(my_dict.items(), key=lambda item: item[1], reverse=True)]
    my_list = my_list[:counts]
    x, y = zip(*my_list)
    plt.figure(figsize=(20, 8), facecolor=None)
    plt.bar(x, y)
    plt.xlabel('word')
    plt.ylabel('counts')
    plt.tight_layout(pad=0)
    plt.savefig(f'../../statistics/{person}_histogram.png')


def count_words_tokens(corpus, person):
    n_words = len(corpus)
    n_types = len(set(corpus.split()))
    print(f"{person.capitalize()}:")
    print(f"Words count: {n_words}")
    print(f"Types count: {n_types}")
    print("-" * 25)
    return n_words, n_types

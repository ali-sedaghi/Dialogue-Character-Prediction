import csv
from metrics import generate_word_cloud, generate_histogram, count_words_tokens


def get_persons_corpus(path):
    persons_corpus = {
        "ross": "",
        "rachel": "",
        "joey": "",
        "chandler": "",
        "monica": "",
        "phoebe": "",
        "all": ""
    }
    file = open(path, encoding='utf-8')
    csv_reader = csv.reader(file)
    for row in csv_reader:
        person = row[0]
        dialogue = row[1]
        if person == "person" and dialogue == "dialogue":
            continue
        persons_corpus[person] += dialogue + ''
        persons_corpus["all"] += dialogue + ''
    file.close()
    return persons_corpus


def main():
    persons_corpus = get_persons_corpus('../../data/dialogues_cleaned.csv')

    person = "ross"
    generate_word_cloud(persons_corpus[person], person)
    generate_histogram(persons_corpus[person], person)
    count_words_tokens(persons_corpus[person], person)

    person = "rachel"
    generate_word_cloud(persons_corpus[person], person)
    generate_histogram(persons_corpus[person], person)
    count_words_tokens(persons_corpus[person], person)

    person = "joey"
    generate_word_cloud(persons_corpus[person], person)
    generate_histogram(persons_corpus[person], person)
    count_words_tokens(persons_corpus[person], person)

    person = "chandler"
    generate_word_cloud(persons_corpus[person], person)
    generate_histogram(persons_corpus[person], person)
    count_words_tokens(persons_corpus[person], person)

    person = "monica"
    generate_word_cloud(persons_corpus[person], person)
    generate_histogram(persons_corpus[person], person)
    count_words_tokens(persons_corpus[person], person)

    person = "phoebe"
    generate_word_cloud(persons_corpus[person], person)
    generate_histogram(persons_corpus[person], person)
    count_words_tokens(persons_corpus[person], person)

    person = "all"
    generate_word_cloud(persons_corpus[person], person)
    generate_histogram(persons_corpus[person], person)
    count_words_tokens(persons_corpus[person], person)


if __name__ == '__main__':
    main()

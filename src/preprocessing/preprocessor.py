from cleaners import remove_whitespaces, to_lower_case, remove_special_chars
from cleaners import remove_short_words, remove_stopwords
from utils import get_columns, get_new_dialogues, write_csv


def preprocess():
    path = '../../data/raw/dialogues.csv'
    persons = get_columns(path, index=0)
    new_dialogues = get_columns(path, index=1)

    # Step 1: Remove white spaces
    path = '../../data/preprocessed/1.white_spaces.csv'
    new_dialogues = get_new_dialogues(new_dialogues, remove_whitespaces)
    write_csv(path, persons, new_dialogues)
    print("Extra whitespaces removed.")

    # Step 2: Lowercase all letters
    path = '../../data/preprocessed/2.lower_case.csv'
    new_dialogues = get_new_dialogues(new_dialogues, to_lower_case)
    write_csv(path, persons, new_dialogues)
    print("All letters converted to lowercase.")

    # Step 3: Remove special characters
    path = '../../data/preprocessed/3.special_chars.csv'
    new_dialogues = get_new_dialogues(new_dialogues, remove_special_chars)
    write_csv(path, persons, new_dialogues)
    print("Special characters removed.")

    # Step 4: Remove short words
    path = '../../data/preprocessed/4.short_words.csv'
    new_dialogues = get_new_dialogues(new_dialogues, remove_short_words)
    write_csv(path, persons, new_dialogues)
    print("Short words removed.")

    # Step 5: Remove stopwords
    path = '../../data/preprocessed/5.stop_words.csv'
    new_dialogues = get_new_dialogues(new_dialogues, remove_stopwords)
    write_csv(path, persons, new_dialogues)
    print("Stop words removed.")

    # Finished
    path = '../../data/dialogues_cleaned.csv'
    write_csv(path, persons, new_dialogues)
    print("Dataset is cleaned.")


if __name__ == '__main__':
    preprocess()
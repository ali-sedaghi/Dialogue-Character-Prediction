import csv


def get_columns(path, index):
    file = open(path, encoding='utf-8')
    csv_reader = csv.reader(file)
    columns = [row[index] for row in csv_reader]
    file.close()
    return columns


def get_new_dialogues(dialogues, preprocessor):
    new_dialogues = []
    for dialogue in dialogues:
        new_dialogue = preprocessor(dialogue)
        new_dialogues.append(new_dialogue)
    return new_dialogues


def write_csv(path, persons, dialogues):
    rows = []
    for p, d in zip(persons, dialogues):
        if d:
            rows.append([p, d])
    with open(path, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    return

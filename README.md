# Dialogue Prediction
In the dialogue prediction task, a model is trained to perdict a character's name based on the given dialogue.
## File directories
- [Phase 1 report file](reports/P1_Report.pdf)
- [Phase 2 report file](reports/P2_Report.pdf)
- [Scripts data file](data/raw/scripts.csv)
- [Raw dialogues data file](data/raw/dialogues.csv)
- [Preprocessed files step by step](data/preprocessed)
- [Cleaned dataset](data/dialogues_cleaned.csv)
- [Statistics before preprocessing](statistics/before_preprocessing)
- [Statistics after preprocessing](statistics/after_preprocessing)
- [Notebooks](notebooks)
- [Model checkpoints](models)

## Dataset
[Friends](https://en.wikipedia.org/wiki/Friends) tv series scripts used as dataset. Friends is an American television sitcom which aired on NBC from September 22, 1994, to May 6, 2004.

There are 6 main characters (classes) in this show:
- Ross
- Rachel
- Joey
- Chandler
- Monica
- Phoebe

The scripts are gathered from [Here](https://www.oocities.org/friends_greatestsitcom).

## How to run
### Requirements
Python packages must be installed:
```bash
pip install -r requirements.txt
```

### Crawler
To run crawler and gather/update dataset:
```bash
cd src/crawler
scrapy crawl scripts -t csv -o ../../data/raw/scripts.csv
scrapy crawl dialogues -t csv -o ../../data/raw/dialogues.csv
```

### Preprocessing
- Step 1: Remove white spaces
- Step 2: Lowercase all letters
- Step 3: Remove special characters
- Step 4: Remove short words
- Step 5: Remove stopwords
```bash
cd src/preprocessing
python preprocessor.py
```

### Statistics
- Each person words count
- Each person types count
- Each person wordcloud
- Each person histogram

Above metrics are extracted for entire scripts before and after preprocessing.
```bash
cd src/statistics
python main.py
```


### Out of repo resources
- [Word clouds](https://drive.google.com/drive/folders/1oEoJabB_qBpmrj-7fJ8PJb7f15PbEM1s?usp=sharing)
- [Model checkpoints](https://drive.google.com/drive/folders/1ns28107R3oX9ywDaTBJpCvSALwxCOQK4?usp=sharing)


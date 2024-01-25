![Frame 1 (5)](https://github.com/raj-pulapakura/bpe/assets/87762282/61af30d7-1c95-4978-8c43-01c13def72ac)

# Byte Pair Encoding

Byte Pair Encoding (BPE) is a deterministic subword tokenization algorithm used by LLMs such as GPT-2. It is essentially an algorithm for converting text into numbers, so that they can be fed into a model.

In this repo I implement the BPE algorithm from scratch, in Python. I ran the BPE algorithm on a corpus of all of Shakespeare works, for 10000 merges, and saved the tokenizer to the `tokenizer.json` file.

The repo contains 4 files (2 scripts, 1 txt, 1 json):

- 🐍 `train.py` Trains a new tokenizer, given the number of merges
- 🐍 `try.py` Provides a cmd interface to tokenize new text
- 📃 `shakespeare.txt` A text file containing all of Shakespeare's works, which I trained the tokenizer on
- 💾 `tokenizer.json` The vocabulary and merge rules of the 10000-merge tokenizer I trained

## 🏎️ Test Drive

### ⬇️ Get the code

1. Clone the repo (or download as zip):

```
git clone https://github.com/raj-pulapakura/bpe.git
```

2. Navigate to the `bpe` directory:

```
cd bpe
```

### 🪄 Tokenize new pieces of text

To try out the tokenizer, run the `try.py` script:

```
python try.py
```

You should see the following output:

```
==================
Byte Pair Encoding
==================

Enter your text: 
```

Just type in your text, and it will be tokenized!

```
==================
Byte Pair Encoding
==================

Enter your text: Well you are quite magnificent!
Integer Tokens: [2642, 127, 231, 4043, 9925, 410, 306, 6531, 2]
Text Tokens: ['Well ', 'you ', 'are ', 'quite ', 'mag', 'ni', 'fi', 'cent', '!']

Enter your text:
```

### 🥷 Train a new tokenizer

To train a new tokenizer, run the `train.py` script, specifying the number of merges you would like to compute (default is 1000):

```
python train.py -m 2000
```

The tokenizer will be trained by default on the `shakespeare.txt` corpus which is already loaded in the directory, but you can swap this out for your own text corpus, as long as it's in a text file. If you do choose to train on your own corpus, make sure you point to the corpus using the `-c` command:

```
python train.py -m 2000 -c amazon_reviews.txt
```

## 🧶 Algorithm Overview

Check out [my YouTube tutorial](https://www.youtube.com/watch?v=BcxJk4WQVIw), where I explain the BPE algorithm in-depth with examples.

The BPE algorithm can be summarized in the following procedure:

- Start with a vocabulary of all the individual characters in the corpus
- Repeat *k* times:
  - 2.1 Choose the two symbols that are most frequently adjacent in the the training corpus, let's say "A" and "B"
  - 2.2 Add a new merged symbol "AB" to the vocabulary
  - 2.3 Replace very adjacent "A" "B" with the single token "AB" in the corpus

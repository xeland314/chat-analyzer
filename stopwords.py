"""
stopwords

The `stopwords` module provides sets of stop words for use in natural language processing tasks.
Stop words are common words that are typically removed from text before further processing, as they
often do not contribute to the meaning of a sentence and can slow down analysis.

This module provides stop words for two languages, Spanish and English, as well as additional stop words
organized into separate files. The stop words are sourced from the Natural Language Toolkit (nltk)
package.

Attributes:
    - `FIRST_LANGUAGE` (str): The first language for which stop words are provided, currently set to "spanish".
    - `SECOND_LANGUAGE` (str): The second language for which stop words are provided, currently set to "english".
    - `IS_INCLUDED_A_SECOND_LANGUAGE` (bool): A flag indicating whether stop words for the second language
    should be included in the stop word set, currently set to True.
    - `STOPWORDS` (set): A set containing the stop words for the selected languages and additional sources.

Additional Files:
    - `alphabet.txt`: Contains a list of words organized by alphabet. These words are used to avoid removing
    stop words that are used as adjectives or adverbs.
    - `punctuation.txt`: Contains a list of punctuation marks. These marks are included as stop words to
    avoid analyzing them as meaningful words.
    - `otherwords.txt`: Contains a list of additional stop words that do not belong to either the Spanish or
    English stop word sets.

Example Usage:
    ```python
    import stopwords

    # Get stop words for the selected language(s)
    stop_words = stopwords.STOPWORDS

    # Filter out stop words from a sentence
    sentence = "This is a sample sentence with some stop words"
    words = sentence.split()
    words_filtered = [word for word in words if word not in stop_words]

    print(words_filtered)  # Output: ["sample", "sentence"]
    ```

Author: Christopher Villamarín (xeland314)
Dependencies: downloaded packages (nltk).
"""

from nltk.corpus import stopwords

FIRST_LANGUAGE = "spanish"
SECOND_LANGUAGE = "english"

IS_INCLUDED_A_SECOND_LANGUAGE = True

STOPWORDS = stopwords.words(FIRST_LANGUAGE)

if IS_INCLUDED_A_SECOND_LANGUAGE:
    STOPWORDS += stopwords.words(SECOND_LANGUAGE)

with open("stopwords/alphabet.txt", "r", encoding="utf8") as file:
    STOPWORDS += [line.replace("\n", "") for line in file]
    STOPWORDS += [line.replace("\n", "").upper() for line in file]

with open("stopwords/punctuation.txt", "r", encoding="utf8") as file:
    STOPWORDS += [line.replace("\n", "") for line in file]

with open("stopwords/otherwords.txt", "r", encoding="utf8") as file:
    STOPWORDS += [line.replace("\n", "") for line in file]

STOPWORDS = set(STOPWORDS)

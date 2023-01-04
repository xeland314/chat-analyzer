try:
    from nltk.corpus import stopwords
except Exception:
    import nltk
    nltk.download('stopwords')
    from nltk.corpus import stopwords

FIRST_LANGUAGE = "spanish"
SECOND_LANGUAGE = "english"

IS_INCLUDED_A_SECOND_LANGUAGE = False
IGNORE_HAHAHA = True

STOPWORDS = stopwords.words(FIRST_LANGUAGE)

if IS_INCLUDED_A_SECOND_LANGUAGE:
    STOPWORDS += stopwords.words(SECOND_LANGUAGE)

if IGNORE_HAHAHA:
    STOPWORDS += [line.replace("\n", "") for line in open("stopwords/hahaha.txt", "r")]

STOPWORDS += [line.replace("\n", "") for line in open("stopwords/alphabet.txt", "r")]
STOPWORDS += [line.replace("\n", "").upper() for line in open("stopwords/alphabet.txt", "r")]
STOPWORDS += [line.replace("\n", "") for line in open("stopwords/otherwords.txt", "r")]
STOPWORDS = set(STOPWORDS)
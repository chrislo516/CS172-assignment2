from nltk.stem.snowball import EnglishStemmer 
import string
def stopword():
    stopwords = []
    #Creating stopwords to a list
    with open('stopwords.txt','r') as f:
        for i in f:
            stopwords.append(i.replace('\n',''))
    f.close()
    return stopwords

ps = EnglishStemmer()
def remove_punc(listing):
    x = listing.translate(str.maketrans('', '', string.punctuation))
    return x

def remove_stopword(listing):
    for i in stopword():
            while i in listing:
                #print(f"Found: {i}")
                listing.remove(i)
    return listing

def stemming(listing):
    new_list_stem = []
    for word in listing:
        new_list_stem.append(ps.stem(word))
    return new_list_stem

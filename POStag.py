import nltk
from pattern.en import tag
def POS(text):
    # tagged_sent = nltk.pos_tag(text,tagset='universal')
    tagged_sent = [tag(sentence) for sentence in text]
    print(tagged_sent)

if __name__ == "__main__":
    text = 'The brown fox is quick and he is jumping over the lazy dog'
    tokens = nltk.word_tokenize(text)
    print(tokens)
    tagged_sent = POS(tokens)

import nltk


def text_to_word(text,abbreviate=True):
    '''

    :param text: 要切分的文本
    :param abbreviate: 是否保留缩写，默认为true
    :return:返回的按句子区分的单词列表
    '''
    sentences = nltk.sent_tokenize(text)
    if not abbreviate:
        pass
    word_list = [nltk.word_tokenize(sentence) for sentence in sentences]
    return word_list

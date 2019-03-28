def remove_puctuation(words):
    '''
    去除标点符号
    :param words:已经切分过的单词列表
    :return: 返回没有标点符号的单词列表
    '''
    import re
    import string
    x = re.compile('[{}]'.format(re.escape(string.punctuation)))
    no_puctuation = []
    for word in words:
        new_token = x.sub(u'',word)
        if not new_token == u'':
            no_puctuation.append(new_token)

    return no_puctuation

def upper_or_lower(text,upper=False,lower=False):
    '''

    :param text: 想要处理的文本
    :param upper: 大写
    :param lower: 小写
    :return:
    '''
    if upper:
        return text.upper()
    if lower:
        return text.lower()

def remove_stopwords(words):
    '''
    处理停用词
    :param words:
    :return: 返回不包含停用词的单词列表
    '''
    from nltk.corpus import stopwords
    stop = set(stopwords.words('english'))
    new_words = []
    for word in words:
        if word not in stop:
            new_words.append(word)
    return new_words

def replace_abbrevation(text):
    '''
    处理缩写
    :param text: 需要处理的文本
    :return:
    '''
    import re
    replacement_patterns=[
        (r"won\'t","will not"),
        (r"can\'t","can not"),
        (r"i\'m","i am"),
        (r"ain\'t","is not"),
        (r"(\w+)\'ll","\g<1> will"),
    ]
    patterns = [(re.compile(regex),repel) for (regex,repel) in replacement_patterns]
    for (pattern,repl) in patterns:
        (text,count) = re.subn(pattern,repl,text)
    return text

def repeat_replace(words):
    '''
    去除单词冲的重复字符
    :param words: 未处理的单词列表
    :return:
    '''
    import re
    from nltk.corpus import wordnet
    repeat_pattern = re.compile(r'(\w*)(\w)\2(\w*)')
    match_substitution = r'\1\2\3'

    def replace(old_word):
        if wordnet.synsets(old_word):  # yong wordnet语料库来查看单词是否存在，若存在，则退出
            return old_word
        new_word = repeat_pattern.sub(match_substitution, old_word)
        return replace(new_word) if new_word != old_word else new_word

    correct_tokens = [replace(word) for word in words]
    return correct_tokens
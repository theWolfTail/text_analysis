from mytokenize import text_to_word
import standard
from POStag import POS

if __name__ == "__main__":
    text = 'The brown fox is quick and he is jumping over the lazy dog'
    # POS(text)
    text = standard.replace_abbrevation(text)
    words = text_to_word(text)
    new_words = []
    for word in words:
        word = standard.remove_puctuation(word)         # 删除标点符号
        word = standard.remove_stopwords(word)          # 删除停用词
        word = standard.repeat_replace(word)            # 重复字符删除
        word = [standard.upper_or_lower(newword,lower=True) for newword in word]        # 大小写转换
        new_words.append(word)
    print(new_words)
    for sentence in new_words:
        POS(sentence)

import nltk
from nltk.corpus import gutenberg
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
import matplotlib

def zipf():
    matplotlib.use('TKAgg')
    fd = FreqDist()
    for text in gutenberg.fileids():
        for word in gutenberg.words(text):
            fd[word] += 1
    ranks = []
    freqs = []
    for rank,word in enumerate(fd):
        ranks.append(rank+1)
        freqs.append(fd[word])
    plt.loglog(ranks,freqs)
    plt.xlabel('frequency(f)',fontsize=14,fontweight='bold')
    plt.ylabel('rank(r)',fontsize=14,fontweight='bold')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    zipf()
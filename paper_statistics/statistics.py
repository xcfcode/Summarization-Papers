from collections import Counter
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud
from nltk import pos_tag

type = "acl22"

if type == "acl20":
    stopwords = [
        "summarization", "for", "and", "in", "a", "to", "with", "the", "as", "from", "of", "an", "on", ";", "-", ":",
        ",", "summarize", "neural"
    ]
elif type == "emnlp20":
    stopwords = [
        "summarization", "for", "and", "in", "a", "to", "with", "the", "as", "from", "of", "an", "on", ";", "-", ":",
        ",", "summarize", "neural"
    ]
elif type == "coling20":
    stopwords = [
        "summarization", "for", "and", "in", "a", "to", "with", "the", "as", "from", "of", "an", "on", ";", "-", ":",
        ",", "summarize", "neural"
    ]
elif type == "aaai21":
    stopwords = [
        "summarization", "for", "and", "in", "a", "to", "with", "the", "as", "from", "of", "an", "on", ";", "-", ":",
        ",", "summarize", "neural"
    ]
elif type == "naacl21":
    stopwords = [
        "summarization", "for", "and", "in", "a", "to", "with", "the", "as", "from", "of", "an", "on", ";", "-", ":",
        ",", "summarize", "neural"
    ]
elif type == "aaai20":
    stopwords = [
        "summarization", "for", "and", "in", "a", "to", "with", "the", "as", "from", "of", "an", "on", ";", "-", ":",
        ",", "summarize", "neural"
    ]
elif type == "nat":
    stopwords = [
        "for", "and", "in", "a", "to", "with", "the", "as", "from", "of", "an", "on", ";", "-", ":",
        ",", "we", "neural", "is", "can", "by", "be", "its", "not", "at", ".", "all", "it", "also", "y"
    ]
elif type == "xcfeng":
    stopwords = [
        "for", "and", "in", "a", "to", "with", "the", "as", "from", "of", "an", "on", ";", "-", ":",
        ",", "we", "neural", "is", "can", "by", "be", "its", "not", "at", ".", "all", "it", "also", "y"
    ]
elif type == "emnlp21" or type == "emnlp21ds" or type == "emnlp21nofindings":
    stopwords = [
        "summarization", "for", "and", "in", "a", "to", "with", "the", "as", "from", "of", "an", "on", ";", "-", ":",
        ",", "summarize", "neural", "abstractive"
    ]
elif type == "acl21":
    stopwords = [
        "summarization", "for", "and", "in", "a", "to", "with", "the", "as", "from", "of", "an", "on", ";", "-", ":",
        ",", "summarize", "neural", "abstractive"
    ]
elif type == "acl22":
    stopwords = [
        "summarization", "for", "and", "in", "a", "to", "with", "the", "as", "from", "of", "an", "on", ";", "-", ":",
        ",", "summarize", "neural", "abstractive"
    ]


def nltk_posatg(words):
    return pos_tag(words)


def filter(pos_word):
    final = []
    for one in pos_word:
        if one[0] not in ["MD", "PRP", "PRP$", "TO", "WDT", "WP", "WP$", "WRB", "LS", "CC", "CD", "DT", "EX", "FW",
                          "IN", "PDT"]:
            final.append(one[0])
    return final


def read_papers(path):
    papers = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                papers.append(line)
    return papers


def common_words(papers):
    counter = Counter()

    for paper in papers:
        title = paper.lower()
        splitted = title.split()
        pos_word = nltk_posatg(splitted)
        splitted = filter(pos_word)
        counter.update(splitted)

    keywords = []
    for w in counter.most_common():
        if w[0] not in stopwords:
            keywords.append(w)

    return keywords


def show_chart(keywords, top_k):
    plt.rcdefaults()
    fig, ax = plt.subplots(figsize=(8, 6))

    key = [k[0] for k in keywords[:top_k]]
    value = [k[1] for k in keywords[:top_k]]
    y_pos = np.arange(len(key))

    ax.barh(y_pos, value, align='center', color='orange', ecolor='black', log=True)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(key, rotation=0, fontsize=10)
    ax.invert_yaxis()

    for i, v in enumerate(value):
        ax.text(v + 1, i + .25, str(v), color='black', fontsize=10)

    plt.show()


def show_wordcloud(keywords):
    wordcloud = WordCloud(max_font_size=100, max_words=100,
                          width=1280, height=640, colormap='magma',
                          background_color="white").generate_from_frequencies(dict(keywords))
    plt.figure(figsize=(16, 8))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()


if __name__ == '__main__':
    print(stopwords)
    papers = read_papers("./res/{}.txt".format(type))
    keywords = common_words(papers)
    show_wordcloud(keywords)

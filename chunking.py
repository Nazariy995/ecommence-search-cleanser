text = nltk.word_tokenize("50 dollar jeans from zappos")
tokenized_sentence = nltk.pos_tag(text)
grammar = r"""
    NP: {<JJ|NN.*>+}
    PP: {<IN>+<(?!IN).*>*<NN.*|NP>+}
"""
cp = nltk.RegexpParser(grammar, loop=2)
result = cp.parse(tokenized_sentence)
from nltk import Tree
def tree2dict(tree):
    return {tree.label(): [tree2dict(t)  if isinstance(t, Tree) else t for t in tree]}
search = tree2dict(result)
for sentence in search["S"]:



#Test


#trial1
grammar = r"""
    NP: {<DT|JJ|NN.*>+}
    PP: {<IN>+<(?!IN).*>*<NN.*>+}
"""

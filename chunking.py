searched = "jeans from zappos for around 50 dollars"
searched  = re.sub(r'(dollar[s]*)','',searched)
text = nltk.word_tokenize(searched)
tokenized_sentence = nltk.pos_tag(text)
grammar = r"""
    PP: {<IN>+<.*>*<NN.*|PP|CD>+}
    NP: {<JJ|NN.*>+}
"""
cp = nltk.RegexpParser(grammar,loop=2)
result = cp.parse(tokenized_sentence)
from nltk import Tree
def tree2dict(tree):
    return {tree.label(): [tree2dict(t)  if isinstance(t, Tree) else t for t in tree]}
search = tree2dict(result)
prices = []
merchants = []
brands = []
search_query = ""
temp_price = temp_brand = temp_merchant = None
def parse_the_dictionary(search,parent_key):
    for key, sentence in search.iteritems():
        for word in sentence:
            if isinstance(word,tuple):
                part_of_speech = re.compile('[JJ|NN|CD]+')
                if part_of_speech.match(word[1]):
                    if price_match(word):
                        prices.append(temp_price)
                        temp_price = None
                    elif merchant_match(word):
                        merchants.append(temp_merchant)
                        temp_merchant=None
                    elif brand_match(word):
                        brands.append(temp_brand)
                        temp_brand = None
                    if key != "PP":
                        search_query+= " "+word[0]#actual value
            elif isinstance(word,dict):
                self.parse_the_dictionary(word)



#Test
price = False
if price:
    print "Price"
merchant = True
elif merchant:
    print "Merchant"

#trial1
grammar = r"""
    NP: {<DT|JJ|NN.*>+}
    PP: {<IN>+<(?!IN).*>*<NN.*>+}
"""


